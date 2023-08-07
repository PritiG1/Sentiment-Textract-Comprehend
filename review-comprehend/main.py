import boto3
import csv
import os

# Set AWS credentials as environment variables
os.environ["AWS_ACCESS_KEY_ID"] = "your_access_id"
os.environ["AWS_SECRET_ACCESS_KEY"] = "your_access_key"

# Specify the AWS region where Rekognition service is available
regionname = 'ap-south-1'

# read the movies CSV and populate the all_notes rray with all the of notes
with open("movies.csv", 'r') as fd:
    reader = csv.DictReader(fd, fieldnames=["ResponseId", "Notes"], dialect='excel')
    all_notes = [ row["Notes"] for row in reader ]

client = boto3.client('comprehend',region_name =regionname)

response = client.batch_detect_sentiment( TextList = all_notes, LanguageCode ='en')

# Write sentiment and notes to 'output.csv' file
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Sentiment', 'Notes']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for result in response["ResultList"]:
        index = result["Index"]
        sentiment = result["Sentiment"]

        writer.writerow({'Sentiment': sentiment, 'Notes': all_notes[index]})
