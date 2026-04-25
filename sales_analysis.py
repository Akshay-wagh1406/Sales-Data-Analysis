# Import pandas library
import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv")

# Display first 5 rows
print("Sales Dataset Preview:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values if any
df.fillna(0, inplace=True)

# Total Revenue
total_revenue = df["Total_Sales"].sum()

# Best Selling Product (by quantity)
best_product = df.groupby("Product")["Quantity"].sum().idxmax()

# Product Revenue
top_revenue_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

# Average Order Value
average_order = df["Total_Sales"].mean()

# Region Wise Sales
region_sales = df.groupby("Region")["Total_Sales"].sum()

# Final Report
print("\n========== SALES REPORT ==========")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Best Selling Product: {best_product}")
print(f"Top Revenue Product: {top_revenue_product}")
print(f"Average Order Value: ₹{average_order:,.2f}")

print("\nRegion Wise Sales:")
print(region_sales)

print("=================================")