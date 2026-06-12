# ==========================================================
# DATA VISUALIZATION PROJECT: E-COMMERCE SALES
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Professional Settings
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10,6)

# 1. LOAD DATASET
# Make sure your excel file name matches exactly
df = pd.read_excel("Dataset for Data Analytics (7).xlsx")

# 2. DATA CLEANING
df.drop_duplicates(inplace=True)
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month_name()

# 3. KPI CALCULATIONS
total_orders = len(df)
total_revenue = df["TotalPrice"].sum()
avg_order_value = df["TotalPrice"].mean()
unique_customers = df["CustomerID"].nunique()

print(f"Total Orders: {total_orders}")
print(f"Total Revenue: {total_revenue:,.2f}")
print(f"Average Order Value: {avg_order_value:.2f}")
print(f"Unique Customers: {unique_customers}")

# 4. VISUALIZATIONS (Auto-saves as PNG)

# Chart 1: Revenue by Product
product_sales = df.groupby("Product")["TotalPrice"].sum().sort_values(ascending=False)
plt.figure(figsize=(10,5))
sns.barplot(x=product_sales.index, y=product_sales.values, hue=product_sales.index, palette="viridis", legend=False)
plt.title("Revenue by Product")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Revenue_by_Product.png")
plt.close()

# Chart 2: Order Status
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="OrderStatus", order=df["OrderStatus"].value_counts().index, hue="OrderStatus", legend=False)
plt.title("Order Status Distribution")
plt.tight_layout()
plt.savefig("Order_Status_Distribution.png")
plt.close()

# Chart 3: Payment Method
payment_method = df["PaymentMethod"].value_counts()
plt.figure(figsize=(8,5))
sns.barplot(x=payment_method.index, y=payment_method.values, hue=payment_method.index, legend=False)
plt.title("Payment Method Analysis")
plt.tight_layout()
plt.savefig("Payment_Method_Analysis.png")
plt.close()

# Chart 4: Monthly Revenue Trend
monthly_revenue = df.groupby(df["Date"].dt.to_period("M"))["TotalPrice"].sum()
monthly_revenue.index = monthly_revenue.index.astype(str)
plt.figure(figsize=(12,5))
plt.plot(monthly_revenue.index, monthly_revenue.values, marker="o", color="blue")
plt.title("Monthly Revenue Trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Monthly_Revenue_Trend.png")
plt.close()

# Chart 5: Referral Source
referral_sales = df.groupby("ReferralSource")["TotalPrice"].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
sns.barplot(x=referral_sales.index, y=referral_sales.values, hue=referral_sales.index, legend=False)
plt.title("Revenue by Referral Source")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Referral_Source_Revenue.png")
plt.close()

# Chart 6: Quantity vs Total Price
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="Quantity", y="TotalPrice")
plt.title("Quantity vs Total Price")
plt.tight_layout()
plt.savefig("Quantity_vs_TotalPrice.png")
plt.close()

# Chart 7: Top 10 Customers
top_customers = df.groupby("CustomerID")["TotalPrice"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_customers.index.astype(str), y=top_customers.values, hue=top_customers.index.astype(str), legend=False)
plt.title("Top 10 Customers by Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Top_10_Customers.png")
plt.close()

# Chart 8: Heatmap
numeric_df = df.select_dtypes(include=np.number)
plt.figure(figsize=(8,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("Correlation_Heatmap.png")
plt.close()

# Save Cleaned Data
df.to_csv("Cleaned_Ecommerce_Data.csv", index=False)
print("PROJECT COMPLETED: All charts and Cleaned CSV saved successfully!")