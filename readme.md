# Sales Data Mart ETL Pipeline

A Python-based ETL pipeline that processes sales, product, and regional data into a PostgreSQL Data Mart for reporting and analytics.

## Business Problem

Organizations often store sales, product, and regional information in separate files, making it difficult to perform consolidated analysis and generate business insights.

This project demonstrates how to build a simple Data Mart by extracting data from multiple CSV files, transforming and validating the datasets, and loading them into PostgreSQL for reporting purposes.

## Features

* Extract data from CSV files
* Data cleansing and validation
* Remove null and duplicate records
* Calculate business metrics
* Load processed data into PostgreSQL
* Create a centralized Data Mart structure

## Technology Stack

* Python
* Pandas
* PostgreSQL
* Psycopg2
* Python Dotenv

## ETL Architecture

```text
sales.csv
product.csv
wilayah.csv
      │
      ▼
   Extract
      │
      ▼
 Transform
      │
      ├─ Remove Null Values
      ├─ Remove Duplicates
      ├─ Calculate Total Sales
      └─ Calculate Discounted Sales
      │
      ▼
      Load
      │
      ▼
 PostgreSQL
      │
      ▼
  Data Mart
```

## Project Structure

```text
Data-Mart/
├── Data/
│   ├── sales.csv
│   ├── product.csv
│   └── wilayah.csv
│
├── Script SQL/
│   └── create_table.sql
│
├── Data_Mart.py
├── .env
└── README.md
```

## Data Transformation

The ETL process performs several transformations:

### Data Quality Checks

* Remove null or missing values
* Remove duplicate records
* Validate dataset consistency

### Business Calculations

```text
total = quantity × price_per_unit

total_with_discount = total - discount
```

## Loading Process

The pipeline automatically:

* Creates PostgreSQL tables if they do not exist
* Loads sales data
* Loads product data
* Loads region (wilayah) data
* Builds a simple Data Mart structure

## Prerequisites

* Python 3.x
* PostgreSQL Database

Required libraries:

```bash
pip install pandas psycopg2-binary python-dotenv
```

## Configuration

Create a `.env` file:

```dotenv
DB_NAME=nama_database
DB_USER=username_database
DB_PASSWORD=password_database
DB_HOST=localhost
DB_PORT=5432
DB_SCHEMA=public
```

## Running the Project

Execute the ETL process:

```bash
python Data_Mart.py
```

After execution, the cleaned and transformed data will be loaded into PostgreSQL.

## Future Improvements

* Incremental loading
* Data warehouse schema (Star Schema)
* Data quality monitoring
* ETL scheduling with Airflow
* Dashboard integration using Power BI or Metabase

## Author

Muhfizh Dzakir

Automation Engineer | QA Automation | SQL | ETL | PostgreSQL
