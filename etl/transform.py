import boto3
import pandas as pd
import os


AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = "ap-southeast-2"


s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

bucket_name = "carbonemissiondata2025"
file_name_co2 = "owid-co2-data.csv"
file_name_energy = "owid-energy-data.csv"

s3.download_file(bucket_name, file_name_co2, '/tmp/owid-co2-data.csv')
s3.download_file(bucket_name, file_name_energy, '/tmp/owid-energy-data.csv')

df_co2 = pd.read_csv('/tmp/owid-co2-data.csv')
df_energy = pd.read_csv('/tmp/owid-energy-data.csv')

df_co2 = df_co2[['country', 'year', 'co2_per_capita']]
df_energy = df_energy[['country', 'year', 'energy_per_capita']]
df_transform = pd.merge(df_co2, df_energy, on=['country', 'year'], how='inner')

df_transform.to_csv('/tmp/transform_data.csv', index=False)

