from sqlalchemy import create_engine
import pandas as pd
import yaml

with open("etl/config.yaml", "r") as file:
    config = yaml.safe_load(file)

DB_URI = config["database"]["uri"]

engine = create_engine(DB_URI)
df = pd.read_csv("/tmp/transform_data.csv")
df.to_sql("pollution_data", engine, if_exists="append", index=False)
print("Data loaded to database successfully")


