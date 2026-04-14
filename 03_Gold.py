# Databricks notebook source
# DBTITLE 1,import time
import time
start = time.time()

# COMMAND ----------

# MAGIC %md
# MAGIC # NOW FOR THE STAR SCHEME APPROACH(FACTS & DIMENSIONS)

# COMMAND ----------

# DBTITLE 1,load silver table
silver_df = spark.table("project_catalog.medallion_project.silver_table")

# COMMAND ----------

# MAGIC %md
# MAGIC ### DIMENSION TABLES

# COMMAND ----------

# MAGIC %md
# MAGIC **dim_product**

# COMMAND ----------

# DBTITLE 1,create dimensions
dim_product = silver_df.select(
    "Product_ID",
    "Product_Category",
    "Unit_Price",
    "Unit_Cost"
).dropDuplicates()

# COMMAND ----------

# MAGIC %md
# MAGIC **dim_customer**

# COMMAND ----------

dim_customer = silver_df.select(
    "Customer_Type"
).dropDuplicates()

# COMMAND ----------

# MAGIC %md
# MAGIC **dim_region**

# COMMAND ----------

dim_region = silver_df.select(
    "Region"
).dropDuplicates()

# COMMAND ----------

# MAGIC %md
# MAGIC **dim_channel**

# COMMAND ----------

dim_channel = silver_df.select(
    "Sales_Channel",
    "Payment_Method"
).dropDuplicates()

# COMMAND ----------

# MAGIC %md
# MAGIC **dim_sales_rep**

# COMMAND ----------

dim_sales_rep = silver_df.select(
    "Sales_Rep"
).dropDuplicates()

# COMMAND ----------

# MAGIC %md
# MAGIC **dim_date**

# COMMAND ----------

dim_date = silver_df.select(
    "Sale_Date"
).dropDuplicates()

# COMMAND ----------

# MAGIC %md
# MAGIC ### **CREATE FACT TABLE**

# COMMAND ----------

fact_sales = silver_df.select(
    "Product_ID",
    "Sale_Date",
    "Sales_Rep",
    "Region",
    "Customer_Type",
    "Sales_Channel",
    "Payment_Method",
    "Sales_Amount",
    "Quantity_Sold",
    "Discount"
)

# COMMAND ----------

# MAGIC %md
# MAGIC ### **save fact table**

# COMMAND ----------

fact_sales.write.mode("overwrite").saveAsTable(
    "project_catalog.medallion_project.fact_sales"
)

# COMMAND ----------

# MAGIC %md
# MAGIC ### SAVE ALL DIMENSION TABLES

# COMMAND ----------

# DBTITLE 1,save all tables
dim_product.write.mode("overwrite").saveAsTable("project_catalog.medallion_project.dim_product")

dim_region.write.mode("overwrite").saveAsTable("project_catalog.medallion_project.dim_region")

dim_customer.write.mode("overwrite").saveAsTable("project_catalog.medallion_project.dim_customer")

dim_channel.write.mode("overwrite").saveAsTable("project_catalog.medallion_project.dim_channel")

dim_sales_rep.write.mode("overwrite").saveAsTable("project_catalog.medallion_project.dim_sales_rep")

dim_date.write.mode("overwrite").saveAsTable("project_catalog.medallion_project.dim_date")

# COMMAND ----------

# DBTITLE 1,optimze fact table
# MAGIC %sql
# MAGIC OPTIMIZE project_catalog.medallion_project.fact_sales

# COMMAND ----------

row_count = spark.table('project_catalog.medallion_project.fact_sales').count()

end = time.time()

print("=== Gold Metrics ===")
print("Rows:", row_count)
print("Execution Time (sec):", end - start)

# COMMAND ----------

