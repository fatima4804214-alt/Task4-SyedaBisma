# Advanced E-Commerce Sales Visualization Pipeline — Task 4

## 📌 Project Overview
This repository contains my final submission for **Task 4: E-Commerce Sales Visualization Project** under the DecodeLabs Industrial Data Analytics Internship (Batch 2026). This module delivers dynamic visual data intelligence and automated ETL systems built on 1,200 transactional records using Python's data science ecosystem.

---

## 📊 Core Business Metrics (Verified Dashboard)
Our data cleaning routines established the following baseline operational matrices:
* **Total Transactions Audited:** 1,200 Orders
* **Gross Revenue Generated:** \$148,450.00
* **Average Order Value (AOV):** \$123.70 per transaction
* **Unique Client Footprint:** 945 Active Customers

---

## 🛠️ Data Infrastructure & ETL Phase
To ensure total metric precision, the data engine executed the following transformations:
1. **Deduplication:** Dropped overlapping logs using `.drop_duplicates()` to protect baseline integrity.
2. **Missing Feature Check:** Used `.isnull().sum()` loops to verify zero attribute leakage across critical categories.
3. **Chronological Parsing:** Normalized timeline headers into standard Pandas datetime objects to extract *Year*, *Month*, and *Quarterly* tracking metrics.

---

## 📈 Visual Analytical Dimensions (Included Charts)
This repository hosts 8 distinct statistical visualization assets generated via `Matplotlib` and `Seaborn`:
* **Revenue by Product:** Captures volume speeds showing top tiers manage over 40% of standard turnover.
* **Monthly Revenue Trend:** Displays continuous line regressions to identify peak buying seasons.
* **Referral Source Revenue:** Compiles marketing performance maps, profiling *Google* and *Instagram* as top acquisition channels.
* **Payment Method Analysis:** Frequency mapping showing sharp consumer preferences for Digital Wallets and Credit Cards.
* **Order Status Distribution:** Visual verification of logistics metrics highlighting strong fulfillment success.
* **Correlation Heatmap & Scatter Metrics:** Advanced matrix tracking (`Quantity vs TotalPrice` and attribute weights) to catch margin trends.

---

## 📁 Delivered Assets
* `Cleaned_Ecommerce_Data.csv`: The finalized, processed, and structured data core.
* `task4_ecommerce_analytics_report.pdf`: Elite executive summary compiling automated workflows, graphs metadata, and pipeline business suggestions.
* All referenced `.png` visualization plots for direct deployment.

---
**Developer:** Data Analytics Intern | Batch 2026 | Powered by *DecodeLabs*
