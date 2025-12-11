# ------------------------------------------
# SALES DATA ANALYSIS PROJECT
# ------------------------------------------
# Step-by-step analysis of a sales dataset:
# - Load data using pandas
# - Clean missing values & duplicates
# - Calculate metrics: total sales, best-selling product, sales by region
# - Generate a simple formatted report
# ------------------------------------------

import pandas as pd

# ----------------------------
# Day 1: Load the dataset
# ----------------------------
df = pd.read_csv("sales_data.csv")

# ----------------------------
# Day 2: Explore the dataset
# ----------------------------
print("🔍 Dataset Shape:", df.shape)
print("\n📌 Columns:", df.columns.tolist())
print("\n📊 Data Types:\n", df.dtypes)

# ----------------------------
# Day 3: Clean the dataset
# ----------------------------

# Handle missing values
df = df.fillna({
    "Product": "Unknown",
    "Region": "Unknown",
    "Quantity": 0,
    "Price": 0,
    "Total_Sales": 0
})

# Remove duplicates
df = df.drop_duplicates()

# ----------------------------
# Day 4: Perform analysis
# ----------------------------

# Metric 1: Total Revenue
total_revenue = df["Total_Sales"].sum()

# Metric 2: Best-selling product
best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()
best_product_sales = df.groupby("Product")["Total_Sales"].sum().max()

# Metric 3: Region with highest sales
best_region = df.groupby("Region")["Total_Sales"].sum().idxmax()
best_region_sales = df.groupby("Region")["Total_Sales"].sum().max()

# Additional Metric: Average order value
average_order = df["Total_Sales"].mean()

# ----------------------------
# Day 5: Create formatted report
# ----------------------------
report = f"""
# 📘 SALES ANALYSIS REPORT

## 📅 Dataset Summary
- Total Rows: {df.shape[0]}
- Total Columns: {df.shape[1]}

## 💰 Key Metrics
- **Total Revenue:** ₹{total_revenue:,.2f}
- **Average Order Value:** ₹{average_order:,.2f}

## 🏆 Best Performing Product
- Product: **{best_product}**
- Sales Amount: ₹{best_product_sales:,.2f}

## 🌍 Best Performing Region
- Region: **{best_region}**
- Sales Amount: ₹{best_region_sales:,.2f}

## ✔️ Cleaning Summary
- Missing values handled
- Duplicates removed

Generated using pandas.
"""

# Save report
with open("analysis_report.md", "w") as f:
    f.write(report)

print("\n✅ Report generated: analysis_report.md")
