import subprocess

print("Running extraction Step...")
subprocess.run(["python", "etl/extract.py"], check=True)

print("Running transformation Step...")
subprocess.run(["python", "etl/transform.py"], check=True)

print("Running load Step...")
subprocess.run(["python", "etl/load.py"], check=True)

print("ETL Pipeline Execution Completed!")
