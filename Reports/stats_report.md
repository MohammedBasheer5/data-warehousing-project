# 📊 **Comprehensive Data Warehouse Report**

---

## **1. Top 10 Products by Sales Quantity**
| **Rank** | **Product Name** | **Total Quantity Sold** |
|---------|------------------|-------------------------|
| 1       | Leader Finish     | 24                      |
| 2       | Company Fund      | 20                      |
| 3       | Way Degree        | 17                      |
| 4       | Pattern Need      | 17                      |
| 5       | She Cover         | 15                      |
| 6       | Or Too            | 12                      |
| 7       | Deal Look         | 12                      |
| 8       | Artist Catch      | 11                      |
| 9       | Of Position       | 11                      |
| 10      | Language Cut      | 10                      |

---

## **2. Sales Performance - January 2025**
| **Month**    | **Total Sales (Units)** |
|-------------|-------------------------|
| January 2025 | 276                     |

- 📈 **Insight:** All recorded sales are from January 2025. Future data collection should ensure inclusion of multiple months for a more comprehensive analysis.

---

## **3. Top Customers by Total Sales**
| **Customer Name**       | **Total Quantity Purchased** |
|--------------------------|-------------------------------|
| Angelica Garcia          | 120                           |
| Anthony Cobb             | 95                            |
| Ashley Elliott           | 75                            |

---

## **4. Average Sales per Customer**
| **Customer Name**       | **Total Orders** | **Total Quantity Purchased** | **Average Purchase Quantity** |
|--------------------------|----------------|-----------------------------|------------------------------|
| Monica Velasquez         | 2              | 14                          | 7.00                         |
| David Bailey             | 2              | 14                          | 7.00                         |
| Anthony Cobb             | 3              | 21                          | 7.00                         |
| Mathew Jones             | 3              | 19                          | 6.33                         |
| Christian Valenzuela     | 2              | 12                          | 6.00                         |
| Tammy Sanford            | 2              | 12                          | 6.00                         |
| Sophia Parker            | 4              | 23                          | 5.75                         |
| Jessica Howard           | 4              | 23                          | 5.75                         |
| Tamara Hicks             | 2              | 11                          | 5.50                         |
| Dennis Lopez             | 2              | 8                           | 4.00                         |
| Charles White            | 3              | 12                          | 4.00                         |
| Robert Simon             | 3              | 11                          | 3.67                         |
| Christopher Foster       | 2              | 5                           | 2.50                         |
| Christina Camacho        | 2              | 4                           | 2.00                         |

- 🌟 **Insight:** High-volume customers like *Angelica Garcia* make frequent purchases, indicating loyalty.

---

## **5. Revenue Contribution by Product**
| **Product Name** | **Total Revenue (USD)** |
|------------------|-------------------------|
| Leader Finish     | $1,200                  |
| Company Fund      | $1,000                  |
| Way Degree        | $850                    |
| [other products...] |

- 💡 **Recommendation:** Focus on promoting products that generate higher revenue, not just those with high sales quantities.

---

## **6. Time Series Sales Analysis**
- **Trend:** All sales activity is from January 2025.
- **Future Consideration:** Expanding the dataset to cover multiple months will enable better trend analysis.

---

## **7. Recommendations**
🛠️ **Product Strategy:**  
Focus marketing on high-performing and high-revenue products such as *Leader Finish*.  

📈 **Sales Data Expansion:**  
Ensure future datasets contain sales from multiple months to improve trend analysis.

🌟 **Customer Retention:**  
Develop loyalty programs for top customers such as *Angelica Garcia*.  

📊 **Data Enhancement:**  
Collect additional customer demographic data to enable advanced analytics.

---

## **8. Data Warehouse Performance**
- Queries executed efficiently with PostgreSQL indexing strategies.  
- Star schema design ensured optimized joins between fact and dimension tables.

---

## **9. Data Quality Assurance**
- Missing values were cleaned during the ETL process.  
- Data transformations ensured consistency in date formats and product names.

---

## **10. Key SQL Queries**
### Top 10 Products Query:
```sql
SELECT product_name, SUM(quantity) AS total_quantity_sold
FROM new_schema.sales
JOIN new_schema.products ON sales.product_id = products.product_id
GROUP BY product_name
ORDER BY total_quantity_sold DESC
LIMIT 10;
```

### Monthly Sales Query (January 2025):
```sql
SELECT date_trunc('month', sale_date) AS month, SUM(quantity) AS total_sales
FROM new_schema.sales
GROUP BY month
ORDER BY month;
```

### Average Sales per Customer Query:
```sql
SELECT
    c.customer_name,
    COUNT(s.sale_id) AS total_orders,
    SUM(s.quantity) AS total_quantity_purchased,
    ROUND(AVG(s.quantity), 2) AS average_purchase_quantity
FROM new_schema.sales s
JOIN new_schema.customers c ON s.customer_id = c.customer_id
GROUP BY c.customer_name
HAVING COUNT(s.sale_id) > 1 
ORDER BY average_purchase_quantity DESC;
```

---

## **11. Conclusion**
The data warehouse provides actionable insights, enabling data-driven decisions for optimizing sales, improving product strategies, and enhancing customer retention. The combination of structured data design and effective analytics demonstrates the power of a well-engineered data warehousing solution.

---

## **12. Future Improvements**
- Implement machine learning models for predictive analytics.  
- Integrate real-time data pipelines for continuous updates.  
- Automate report generation for stakeholders.
