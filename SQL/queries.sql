-- Total Sales by Product
SELECT p.product_name, SUM(f.quantity) AS total_quantity, SUM(f.total_price) AS total_sales
FROM dw_schema.fact_sales f
JOIN dw_schema.dim_products p ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sales DESC;

-- Total Sales by Customer
SELECT c.customer_name, SUM(f.total_price) AS total_spent
FROM dw_schema.fact_sales f
JOIN dw_schema.dim_customers c ON f.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY total_spent DESC;

-- Monthly Sales Trends
SELECT d.year, d.month, SUM(f.total_price) AS total_sales
FROM dw_schema.fact_sales f
JOIN dw_schema.dim_date d ON f.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;

-- Top 5 Best-Selling Products
SELECT p.product_name, SUM(f.quantity) AS total_sold
FROM dw_schema.fact_sales f
JOIN dw_schema.dim_products p ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC
LIMIT 5;

-- Customer with the Highest Purchases
SELECT c.customer_name, COUNT(f.sale_id) AS total_orders, SUM(f.total_price) AS total_spent
FROM dw_schema.fact_sales f
JOIN dw_schema.dim_customers c ON f.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY total_spent DESC
LIMIT 1;
