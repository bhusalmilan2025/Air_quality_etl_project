## Project Overview
### Objective:
The objective of this project is to process and analyze air quality, CO2 emissions, and energy consumption data. This data will be extracted from local CSV files, transformed using a Python-based ETL pipeline, and then loaded into a PostgreSQL database hosted on Amazon RDS. The project will involve creating an automated ETL pipeline and deploying it using Docker and AWS ECS to handle scalable processing of environmental data.

### Consumers:
The key users of the data and results are:
- **Data Analysts**: They will analyze the air quality, CO2 emissions, and energy consumption data to identify patterns, correlations, and trends.
- **Environmental Researchers**: They will use this data to conduct research on global pollution, CO2 emissions, and energy consumption to understand the impact on climate change.

These users will access the data via SQL queries, Python scripts, or through data visualization tools like Tableau, PowerBI, or Jupyter Notebooks.

---

## Key Questions:
The following questions are the focus of this project, which will guide data analysis and reporting:

- **CO2 Emissions:**
  - What is the global trend of CO2 emissions over the years?
  - Which countries emit the most CO2 each year?
  - How do CO2 emissions correlate with energy consumption across different regions?
- **Energy Consumption:**
  - What is the global distribution of energy consumption by source?
  - Which regions use more renewable energy versus fossil fuels?
- **ETL Pipeline:**
  - How frequently will the ETL pipeline run to ensure up-to-date data?
  - How can the ETL pipeline be automated to run periodically?

---

## Source Datasets:
The following datasets will be sourced for the ETL pipeline:

| Source Name              | Source Type | 
|--------------------------|-------------|
| **Local CSV (CO2 Emissions)** | CSV File    
| **Local CSV (Energy Data)**  | CSV File    
| **S3 Bucket (CO2, Energy)**  | S3 Bucket  
| **PostgreSQL (RDS Database)**| Relational Database 

---

## Solution Architecture:

The solution is built using AWS services and Docker, which facilitates easy scaling and deployment. The architecture will consist of the following components:

### Data Extraction:
- **Source**: The data will initially be available as local CSV files (CO2 emissions, Energy data).
- **Destination**: The data will be uploaded to an **Amazon S3 bucket** for storage and access.

### Data Transformation:
The transformation is performed using a **Python-based ETL pipeline**, which involves:
### 1. Column Selection  
- From the **CO2 emissions dataset**, only the following columns are retained:  
  - `country`  
  - `year`  
  - `co2_per_capita`  
- From the **Energy consumption dataset**, only the following columns are kept:  
  - `country`  
  - `year`  
  - `energy_per_capita`  

### 2. Merging Datasets  
- The **CO2 emissions dataset** and the **Energy consumption dataset** are merged on `country` and `year` using an **inner join** to ensure that only data points present in both datasets are retained.  

### 3. Saving Transformed Data  
- The transformed dataset is saved as `transform_data.csv` in the `/tmp/` directory for further processing and loading into the database.  

### Data Loading:
- **Destination**: Transformed data will be loaded into a **PostgreSQL** database hosted on **AWS RDS** for further analysis and storage.

### Deployment:
- **Docker**: The Python ETL pipeline will be containerized using **Docker**, enabling portability and ease of deployment across different environments.
- **Amazon ECS**: The containerized application will be deployed using **AWS Elastic Container Service (ECS)**, which will manage the execution and scaling of containers.

---
## Final Deliverables:
- Fully implemented **ETL pipeline** in Python for extracting, transforming, and loading data.
- **Dockerized** version of the ETL pipeline deployed on **AWS ECS**.
- Transformed data loaded into a **PostgreSQL database** hosted on **AWS RDS**.
- **Project documentation** including:
  - **README** detailing setup and usage.
  - **Project Plan** outlining the process and timeline.


---

## Additional Information:
- **Technology Stack**:
  - **Python** for the ETL pipeline.
  - **PostgreSQL** for relational database management.
  - **AWS** for cloud infrastructure (S3, RDS, ECS).
  - **Docker** for containerization.
  - **SQLAlchemy** for database interaction in Python.
