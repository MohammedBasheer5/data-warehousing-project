import pandas as pd
import psycopg2
from psycopg2 import sql, OperationalError

# Database connection settings
host = 'localhost'
user = 'postgres'
password = '123qw'
database = 'data_warehouse'

def load_data_to_postgres(filepath, schema_name, table_name):
    conn = None
    try:
        # Connect to the database
        conn = psycopg2.connect(
            dbname=database,
            user=user,
            password=password,
            host=host
        )
        cursor = conn.cursor()

        # Read the CSV file with the correct delimiter
        data = pd.read_csv(filepath, sep=",") 

        print(f"Column names: {data.columns}")

        # Dynamically create the insert query
        columns = list(data.columns)
        insert_query = sql.SQL("INSERT INTO {}.{} ({}) VALUES ({})").format(
            sql.Identifier(schema_name),
            sql.Identifier(table_name),
            sql.SQL(', ').join(map(sql.Identifier, columns)),
            sql.SQL(', ').join(sql.Placeholder() for _ in range(len(columns)))
        )

        # Insert data into the table
        for row in data.itertuples(index=False, name=None):
            cursor.execute(insert_query, row)

        # Commit the transaction
        conn.commit()
        print(f"Data successfully loaded into '{schema_name}.{table_name}' from file '{filepath}'.")

    except pd.errors.EmptyDataError:
        print(f"Error: The file '{filepath}' is empty.")
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' does not exist.")
    except OperationalError as e:
        print(f"Connection error while loading data into '{schema_name}.{table_name}': {e}")
    except Exception as e:
        print(f"An error occurred while loading data into '{schema_name}.{table_name}': {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    try:
        # Load data into tables in the new schema
        load_data_to_postgres(r"C:\Users\Subeh\Desktop\Project_DataWS\customers_data.csv", "new_schema", "customers")
        load_data_to_postgres(r"C:\Users\Subeh\Desktop\Project_DataWS\products_data.csv", "new_schema", "products")
        load_data_to_postgres(r"C:\Users\Subeh\Desktop\Project_DataWS\sales_data.csv", "new_schema", "sales")

    except Exception as e:
        print(f"A critical error occurred: {e}")
