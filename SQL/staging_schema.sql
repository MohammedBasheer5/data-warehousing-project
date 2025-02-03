CREATE SCHEMA IF NOT EXISTS staging;

-- Staging Table for Customers
CREATE TABLE staging.customers (
    customer_id INT,
    customer_name TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    city TEXT,
    country TEXT
);

-- Staging Table for Products
CREATE TABLE staging.products (
    product_id INT,
    product_name TEXT,
    category TEXT,
    price NUMERIC
);

-- Staging Table for Sales
CREATE TABLE staging.sales (
    sale_id INT,
    customer_id INT,
    product_id INT,
    quantity INT,
    total_price NUMERIC,
    sale_date DATE
);