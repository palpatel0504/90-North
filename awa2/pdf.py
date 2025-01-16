import json
import boto3
import base64
import os

s3 = boto3.client("s3")
BUCKET_NAME = "your-s3-bucket-name"  # Replace with your actual S3 bucket name

def lambda_handler(event, context):
    try:
        file_content = event.get("file_content")  # Base64 encoded file content
        file_name = event.get("file_name", "uploaded_file.pdf")  # Default file name
        
        if not file_content:
            return {
                "statusCode": 400,
                "body": json.dumps("Error: No file content provided")
            }

        # Decode the Base64 string
        file_data = base64.b64
