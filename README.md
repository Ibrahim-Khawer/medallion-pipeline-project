Medallion Architecture Pipeline (Databricks)
Overview

This project implements a Medallion Architecture using Databricks and Delta Lake to transform raw sales data into an analytics-ready Star Schema model.

Pipeline Structure
Bronze Layer (Raw Data)
CSV data ingestion from volume storage
Stored as Delta table
No transformations applied
Silver Layer (Cleaned Data)
Removes duplicates
Data cleaning and preparation
Optimized using OPTIMIZE and ZORDER
Gold Layer (Star Schema)
Implements Fact and Dimension model
Fact table contains transaction-level sales data
Dimension tables:
Product
Region
Customer
Channel
Sales Representative
Date
Dataset Columns

Product_ID
Sale_Date
Sales_Rep
Region
Sales_Amount
Quantity_Sold
Product_Category
Unit_Cost
Unit_Price
Customer_Type
Discount
Payment_Method
Sales_Channel

Technologies Used

Databricks
Delta Lake
PySpark
SQL

Metrics

Execution Time (seconds)

Bronze: 55.76
Silver: 8.31
Gold: 20.38

Data Size (MB)

Bronze: 0.022
Silver: 0.022
Gold: 0.002

Data Movement

Bronze → Silver: 1000 → 1000
Silver → Gold: 1000 → 1000
Key Learnings

Medallion architecture design
Star schema modeling
Data transformation pipelines
Delta Lake optimization (OPTIMIZE, ZORDER)
Performance measurement techniques
