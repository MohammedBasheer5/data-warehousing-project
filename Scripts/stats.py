import pandas as pd
from sqlalchemy import create_engine

# Database connection settings
host = 'localhost'
user = 'postgres'
password = '123qw'
database = 'data_warehouse'
schema = 'dw_schema'

# Create a connection engine using SQLAlchemy
engine = create_engine(f'postgresql://{user}:{password}@{host}/{database}')

def execute_query(query):
    """Execute an SQL query and return results as a DataFrame"""
    try:
        # Use SQLAlchemy engine with pandas to read SQL query results
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

# SQL queries to extract statistics
queries = {
    "total_sales_per_product": f"""
        SELECT p.product_name, SUM(s.total_price) AS total_sales
        FROM {schema}.fact_sales s
        JOIN {schema}.dim_products p ON s.product_id = p.product_id
        GROUP BY p.product_name
        ORDER BY total_sales DESC;
    """,
    "top_customers": f"""
        SELECT c.customer_name, SUM(s.total_price) AS total_spent
        FROM {schema}.fact_sales s
        JOIN {schema}.dim_customers c ON s.customer_id = c.customer_id
        GROUP BY c.customer_name
        ORDER BY total_spent DESC
        LIMIT 10;
    """,
    "sales_by_date": f"""
        SELECT d.full_date, SUM(s.total_price) AS total_sales
        FROM {schema}.fact_sales s
        JOIN {schema}.dim_date d ON s.date_id = d.date_id
        GROUP BY d.full_date
        ORDER BY d.full_date;
    """
}

if __name__ == "__main__":
    # Iterate through the queries dictionary and execute each query
    for key, query in queries.items():
        print(f"\n--- {key.replace('_', ' ').upper()} ---")
        result = execute_query(query)
        if result is not None:
            # Print the result DataFrame
            print(result)
