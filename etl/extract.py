import boto3
import pandas as pd
import os

#AWS S3 configuration

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = "ap-southeast-2"
BUCKET_NAME = "carbonemissiondata2025"

# Initialize s3 client

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

def extract_data():
    try:
        df_co2 = pd.read_csv('/Users/milanb/Downloads/Co2_Energy Today/owid-co2-data.csv')
        df_energy = pd.read_csv('/Users/milanb/Downloads/Co2_Energy Today/owid-energy-data.csv')

        s3.upload_file('/Users/milanb/Downloads/Co2_Energy Today/owid-co2-data.csv', BUCKET_NAME, 'owid-co2-data.csv')
        s3.upload_file('/Users/milanb/Downloads/Co2_Energy Today/owid-energy-data.csv', BUCKET_NAME, 'owid-energy-data.csv')

        print("Data uploaded to S3")
    except Exception as e:
        print(f"error extracting data - {e}")

if __name__ == '__main__':
    extract_data()