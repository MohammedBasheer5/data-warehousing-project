# Retail Data Warehouse Project

## Project Overview

This project is designed to create a Data Warehouse for analyzing sales data, helping business owners understand market changes and make informed decisions based on data. PostgreSQL is used for data organization and analysis, with Python handling the extraction, transformation, and loading (ETL) processes.

## Project Objectives

- **Data Ingestion**: Load data from various sources into the database.
- **Data Transformation**: Clean and process the data for analysis.
- **Data Warehouse Design**: Implement a Star or Snowflake Schema in PostgreSQL.
- **Data Analysis**: Generate key statistics and insights from the stored data.

## Project Structure

```
data-warehousing-project/
├── README.md              # Project overview and setup instructions
├── .gitignore             # Specifies files and directories to exclude from Git
├── requirements.txt       # Project dependencies
├── data/                  # Raw and processed data
│   ├── raw/               # Extracted raw data files
│   └── processed/         # Cleaned and transformed data files
├── scripts/               # Python scripts for ETL and modeling
│   ├── ingestion.py       # Extract and load data into PostgreSQL
│   ├── transformation.py  # Clean and transform data
│   ├── modeling.py        # Create the Data Warehouse schema and load data
│   └── stats.py           # Analyze data and generate insights
├── sql/                   # SQL scripts for schema creation and queries
│   ├── staging_schema.sql # Staging database schema
│   ├── dw_schema.sql      # Data Warehouse schema
│   └── queries.sql        # Analytical queries
├── notebooks/             # Optional Jupyter notebooks for exploration
│   └── exploration.ipynb  # Data exploration notebook
├── config/                # Configuration files for APIs and the database
│   ├── db_config.json     # Database connection details
│   └── api_config.json    # API keys and configurations
└── reports/               # Reports and analysis
    └── stats_report.md    # Summary of findings and insights
```

## Installation & Setup

### 1. Clone the repository:

```bash
git clone https://github.com/MohammedBasheer5/Data-Warehouse.git
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Requirements:

- **PostgreSQL**: To store and manage data.
- **Jupyter Notebook**: For data exploration and analysis.
- **Python Libraries**:

```bash
pip install psycopg2 pandas sqlalchemy matplotlib scikit-learn
```

### 4. Setup Database:

- Install PostgreSQL and create a new database (e.g., `dw`).
- Run the SQL scripts to create the necessary tables.

### 5. Run the ETL pipeline:

```bash
python scripts/ingestion.py
python scripts/transformation.py
python scripts/modeling.py
python scripts/stats.py
```

## Example Query:

```sql
SELECT product_name, SUM(total_price) AS total_sales
FROM dw_schema.fact_sales s
JOIN dw_schema.dim_products p ON s.product_id = p.product_id
GROUP BY product_name
ORDER BY total_sales DESC;
```

## Contact Information

- **Name**: MohammedBasheer5
- **Email**: [mb11990011@gmail.com](mailto:mb11990011@gmail.com)
- **Phone**: +972597994896