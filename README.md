## Medallion Architecture Pipeline (Databricks)

## Overview
This project implements a Medallion Architecture using Databricks and Delta Lake to transform raw sales data into analytics-ready insights.

---

## Pipeline Structure

### Bronze Layer
- Raw data ingestion from CSV file
- Stored as Delta table
- No transformations applied

### Silver Layer
- Removes duplicates
- Cleans dataset
- Optimized using ZORDER

### Gold Layer
- Aggregates data using GROUP BY
- Generates business KPIs:
  - Total Sales
  - Total Quantity Sold

---

## Dataset
Sales dataset containing:
- Region
- Product Category
- Customer Type
- Sales Channel
- Sales Amount
- Quantity Sold



---

## ⚙️ Technologies Used
- Databricks
- Delta Lake
- PySpark
- SQL

---

## Metrics

### Execution Time (seconds)
- Bronze Layer: 55.76 sec  
- Silver Layer: 8.31 sec  
- Gold Layer: 20.38 sec  


### Data Size(MB)
- Bronze Layer: 0.022 MB  
- Silver Layer: 0.022 MB  
- Gold Layer: 0.002 MB  

### Data Movement
- Bronze → Silver: 1000 → 1000  
- Silver → Gold: 1000 → 64  

---

## Key Learnings
- Medallion architecture design
- Data transformation pipelines
- Delta Lake optimization (OPTIMIZE + ZORDER)
- Performance measurement (execution time + data size)
- Aggregation-based modeling
