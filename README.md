# CO2 Emissions, and Energy Consumption ETL Pipeline

## Overview
The objective of this project is to process and analyze air quality, CO2 emissions, and energy consumption data. The data is extracted from local CSV files, transformed using Python ETL scripts, and loaded into a PostgreSQL database hosted on Amazon RDS. The entire pipeline is containerized with Docker and deployed on AWS ECS.

## Project Setup

### Prerequisites
- Docker
- Python 3.x
- AWS Account (for ECS, RDS, S3)
- PostgreSQL
- IAM Permissions for AWS S3, RDS, and ECS

### Installation
1. **Clone the repository**:
   ```bash
   git clone https://https://github.com/bhusalmilan2025/Air_quality_etl_project
   cd air-quality-etl-project
