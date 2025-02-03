import pandas as pd
import os

print("The libraries are working properly.")
#_______________________________________________________________________________

# Define desktop path for saving files
desktop_path = r"C:\Users\Subeh\Desktop"

# Load datasets
customers_df = pd.read_csv('customers_data.csv')
products_df = pd.read_csv('products_data.csv')
sales_df = pd.read_csv('sales_data.csv')

print(customers_df.columns)
print(customers_df.shape)
print(customers_df.head())

# Clean Customers Data
customers = pd.DataFrame(customers_df).drop_duplicates().dropna()

if 'registration_date' not in customers.columns:
    customers['registration_date'] = pd.date_range(start='2022-01-01', periods=len(customers))
else:
    customers['registration_date'] = pd.Timestamp.today()

# Save cleaned customers data
customers_output_file = os.path.join(desktop_path, "cleaned_customers.csv")
customers.to_csv(customers_output_file, index=False)
print(f"Data transformed and saved successfully to {customers_output_file}!")

#_______________________________________________________________________________

print(products_df.columns)
print(products_df.shape)
print(products_df.head())

# Clean Products Data
products = pd.DataFrame(products_df).drop_duplicates().dropna()
products['product_id'] = products['product_id'].astype(int)
products['price'] = products['price'].astype(float)

# Save cleaned products data
products_output_file = os.path.join(desktop_path, "cleaned_products.csv")
products.to_csv(products_output_file, index=False)
print(f"Products data transformed and saved successfully to {products_output_file}!")

#_______________________________________________________________________________

print(sales_df.columns)
print(sales_df.shape)
print(sales_df.head())

# Clean Sales Data
sales = pd.DataFrame(sales_df).drop_duplicates().dropna()
sales['sale_date'] = pd.to_datetime(sales['sale_date'], errors='coerce')
sales['sale_price'] = sales['total_price'] / sales['quantity']
sales['product_id'] = sales['product_id'].astype(int)
sales['customer_id'] = sales['customer_id'].astype(int)

# Save cleaned sales data
sales_output_file = os.path.join(desktop_path, "cleaned_sales.csv")
sales.to_csv(sales_output_file, index=False)
print(f"Sales data transformed and saved successfully to {sales_output_file}!")

#_______________________________________________________________________________

# Merge Data
sales_products = pd.merge(sales, products, on='product_id', how='inner')
final_data = pd.merge(sales_products, customers, on='customer_id', how='inner')

# Save final integrated data
final_output_file = os.path.join(desktop_path, "final_transformed_data.csv")
final_data.to_csv(final_output_file, index=False)

print("Data integration completed and saved successfully!")
print(final_data.shape)
print(final_data.head(10))

#_______________________________________________________________________________
