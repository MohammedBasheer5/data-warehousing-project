CREATE SCHEMA IF NOT EXISTS dw_schema;

-- Dimension Table: Customers
CREATE TABLE dw_schema.dim_customers (
    customer_id INT PRIMARY KEY,
    customer_name TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    city TEXT,
    country TEXT
);

-- Dimension Table: Products
CREATE TABLE dw_schema.dim_products (
    product_id INT PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price NUMERIC
);

-- Dimension Table: Date
CREATE TABLE dw_schema.dim_date (
    date_id SERIAL PRIMARY KEY,
    full_date DATE UNIQUE,
    year INT,
    quarter INT,
    month INT,
    day INT,
    weekday TEXT
);

-- Fact Table: Sales
CREATE TABLE dw_schema.fact_sales (
    sale_id INT PRIMARY KEY,
    customer_id INT REFERENCES dw_schema.dim_customers(customer_id),
    product_id INT REFERENCES dw_schema.dim_products(product_id),
    date_id INT REFERENCES dw_schema.dim_date(date_id),
    quantity INT,
    total_price NUMERIC
);
