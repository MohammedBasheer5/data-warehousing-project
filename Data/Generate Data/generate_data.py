import os
import pandas as pd
from faker import Faker
import random

def generate_data():
    faker = Faker()

    # Define the desktop path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # 1. Generate customer data
    customers = []
    for i in range(1, 51):  # 50 rows
        customer = {
            "customer_id": i,
            "customer_name": faker.name(),
            "email": faker.email(),
            "phone": faker.phone_number(),
            "address": faker.address().replace('\n', ', '),
            "city": faker.city(),
            "country": faker.country()
        }
        customers.append(customer)

    customers_df = pd.DataFrame(customers)
    customers_file = os.path.join(desktop_path, "customers_data.csv")
    customers_df.to_csv(customers_file, index=False)
    print(f"Saved 'customers_data.csv' to {customers_file}")

    # 2. Generate product data
    products = []
    categories = ['Electronics', 'Clothing', 'Home Appliances', 'Books', 'Toys']
    for i in range(1, 51):  # 50 rows
        product = {
            "product_id": i,
            "product_name": faker.word().capitalize() + " " + faker.word().capitalize(),
            "category": random.choice(categories),
            "price": round(random.uniform(5, 500), 2)
        }
        products.append(product)

    products_df = pd.DataFrame(products)
    products_file = os.path.join(desktop_path, "products_data.csv")
    products_df.to_csv(products_file, index=False)
    print(f"Saved 'products_data.csv' to {products_file}")

    # 3. Generate sales data
    sales = []
    for i in range(1, 51):  # 50 rows
        customer_id = random.randint(1, 50)
        product_id = random.randint(1, 50)
        quantity = random.randint(1, 10)
        price = products_df.loc[product_id - 1, "price"]  # Get product price
        total_price = round(price * quantity, 2)
        sale = {
            "sale_id": i,
            "customer_id": customer_id,
            "product_id": product_id,
            "quantity": quantity,
            "total_price": total_price,
            "sale_date": faker.date_this_year()
        }
        sales.append(sale)

    sales_df = pd.DataFrame(sales)
    sales_file = os.path.join(desktop_path, "sales_data.csv")
    sales_df.to_csv(sales_file, index=False)
    print(f"Saved 'sales_data.csv' to {sales_file}")

if __name__ == "__main__":
    generate_data()
