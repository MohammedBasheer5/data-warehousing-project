import psycopg2
from psycopg2 import sql, OperationalError

# Database connection settings
DB_CONFIG = {
    "host": "localhost",
    "dbname": "data_warehouse",
    "user": "postgres",
    "password": "123qw",
    "port": "5432"
}

def create_schema():
    """Create the schema for the data warehouse"""
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        cursor.execute("CREATE SCHEMA IF NOT EXISTS dw_schema;")
        conn.commit()
        print("Schema 'dw_schema' created successfully.")

    except OperationalError as e:
        print(f"Database connection error: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

def create_tables():
    """Create tables for the data warehouse"""
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Table creation queries
        tables = {
            "dim_customers": """
                CREATE TABLE IF NOT EXISTS dw_schema.dim_customers (
                    customer_id SERIAL PRIMARY KEY,
                    customer_name TEXT NOT NULL,
                    email TEXT UNIQUE,
                    phone TEXT,
                    address TEXT
                );
            """,
            "dim_products": """
                CREATE TABLE IF NOT EXISTS dw_schema.dim_products (
                    product_id SERIAL PRIMARY KEY,
                    product_name TEXT NOT NULL,
                    category TEXT,
                    price NUMERIC(10,2) NOT NULL
                );
            """,
            "dim_date": """
                CREATE TABLE IF NOT EXISTS dw_schema.dim_date (
                    date_id SERIAL PRIMARY KEY,
                    full_date DATE UNIQUE NOT NULL,
                    year INTEGER NOT NULL,
                    month INTEGER NOT NULL,
                    day INTEGER NOT NULL
                );
            """,
            "fact_sales": """
                CREATE TABLE IF NOT EXISTS dw_schema.fact_sales (
                    sale_id SERIAL PRIMARY KEY,
                    customer_id INTEGER,
                    product_id INTEGER,
                    date_id INTEGER,
                    quantity INTEGER NOT NULL,
                    total_price NUMERIC(10,2) NOT NULL,
                    FOREIGN KEY (customer_id) REFERENCES dw_schema.dim_customers(customer_id),
                    FOREIGN KEY (product_id) REFERENCES dw_schema.dim_products(product_id),
                    FOREIGN KEY (date_id) REFERENCES dw_schema.dim_date(date_id)
                );
            """
        }

        # Execute table creation
        for table_name, query in tables.items():
            cursor.execute(query)
            print(f"Table '{table_name}' created successfully.")

        conn.commit()

    except OperationalError as e:
        print(f"Database connection error: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    create_schema()  # Create schema
    create_tables()  # Create tables
