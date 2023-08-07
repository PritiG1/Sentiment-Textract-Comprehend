# Sentiment-Textract-Comprehend
This repository explores leveraging Amazon Textract for handwritten movie review analysis, followed by sentiment analysis using Amazon Comprehend.
By following the steps outlined here, you'll be able to transform raw handwritten content into structured data, perform sentiment analysis, and derive valuable insights.


## Introduction

In the digital age, deciphering the sentiments and insights hidden within handwritten reviews is no longer a challenge thanks to the capabilities offered by Amazon Textract and Comprehend. This repository guides you through the process of setting up your environment, using Amazon Textract to extract handwritten text from images, employing Amazon Comprehend for sentiment analysis, and visualizing the results.

## Medium Article

To gain a deeper understanding of the concepts and techniques covered in this repository, don't miss my accompanying Medium article: 

## Repository Structure

This repository is organized into the following directories:

1. **install_boto**: Contains a Jupyter Notebook (`install_boto.ipynb`) that provides bash commands to install the Boto3 library, the AWS SDK for Python.
2. **review_textract**: Contains the Python script to use Amazon Textract for extracting handwritten movie reviews from images and recording the output in the `movies.csv` file. It also includes the folder `raw_images` with sample images for demonstration.
3. **review_comprehend**: Contains the Python script to use Amazon Comprehend for sentiment analysis on movie reviews. It generates sentiment analysis outputs and a count plot, both of which are useful for deriving insights.

## Getting Started

Follow these steps to get started with the repository:

1. Install Boto3 by referring to the commands in `install_boto.ipynb`.
2. Navigate to the `review_textract` directory and run `review_textract.py` to extract handwritten movie reviews and record the output in `movies.csv`.
3. Move to the `review_comprehend` directory and run `review_comprehend.py` to perform sentiment analysis on the extracted movie reviews. This script also generates sentiment analysis outputs and a count plot.

## Acknowledgments

I acknowledge Coursera's Introduction to AWS course for the dataset and training. Happy analyzing!

For any questions or feedback, feel free to reach out to me.
