import glob # This library helps in finding all the pathnames matching a specified pattern.
import boto3 #  It is the AWS SDK for Python, allowing interaction with various AWS services.
import json # It provides functionality for working with JSON data.
import csv #This library provides functionality for reading and writing CSV files.
import sys #
import os

# Set AWS credentials as environment variables
os.environ["AWS_ACCESS_KEY_ID"] = "Your_Access_id"
os.environ["AWS_SECRET_ACCESS_KEY"] = "Your_Access_key"

# Specify the AWS region where service is available
regionname = 'ap-south-1'

#Create an empty list csv_array to store the extracted data from the images in a CSV format:
csv_array = []

#Create a Textract client:
client = boto3.client('textract',region_name = regionname)

#Loop through each JPEG file in the 'raw_images' folder:
for filename in glob.glob('raw_images/*.jpg'):
    csv_row = {}
    print(f"Processing: {filename}")
    with open(filename, 'rb') as fd:
        file_bytes = fd.read()

#Use AWS Textract to analyze the document and extract the specified features (queries) from the image:
#In this case, Textract is configured to extract two queries: one for the "ResponseId" and another for the "Notes".
    response = client.analyze_document(
        Document={'Bytes': file_bytes},
        FeatureTypes=["QUERIES"],
        QueriesConfig={
            'Queries': [
                {'Text': 'What is the response id', 'Alias': 'ResponseId'},
                {'Text': 'What are the notes?', 'Alias': 'Notes'},
            ]
        }
    )
    
    # Loop through each block in the Textract response
    for block in response["Blocks"]:
        # Check if the block type is a QUERY
        if block["BlockType"] == "QUERY":
            # Get the alias (name) of the query from the 'Alias' field of the current query block
            query_alias = block["Query"]["Alias"]

            # Find the ID of the corresponding answer block for the current query
            answer_id = next(rel["Ids"] for rel in block["Relationships"] if rel['Type'] == "ANSWER")[0]

            # Extract the text of the answer from the 'Blocks' list using the obtained answer ID
            answer_text = next(b for b in response["Blocks"] if b["Id"] == answer_id)["Text"]

            # Populate the 'csv_row' dictionary with the extracted query alias and its corresponding answer text
            csv_row[query_alias] = answer_text
    
    
    csv_array.append(csv_row)

# Write the CSV data to a file
with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ["ResponseId", "Notes"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel')
    writer.writeheader()
    for row in csv_array:
        writer.writerow(row)

print("CSV data has been written to output.csv")    
