<img width="1048" height="540" alt="Pizza Digram" src="https://github.com/user-attachments/assets/9a7be9c0-d5d0-498e-8152-8eeda8bcfa77" /># 🍕 PizzaOps-DataPipeline-AWS

## 📌 Project Overview
PizzaOps-DataPipeline-AWS is a cloud-native batch analytics pipeline designed for a fictional multi-store pizza retail chain. It simulates real-world retail operations by ingesting, transforming, and analyzing operational data such as orders, inventory, and discounts. The system delivers actionable insights and automated alerts using AWS services.

## 🔥 Problem Statement
Multi-store pizza chains face challenges in managing fragmented data, delayed insights, and manual operations. This project addresses:
- Real-time inventory tracking
- Discount campaign effectiveness
- Store-wise performance analysis
- Automated alerting for operational risks

## 🧭 Architecture Diagram

![Pizza Digram](images/Pizza%20Digram%20.png) 


## 🏗️ Architecture Overview
- **Amazon RDS**: Stores raw operational data
- **AWS Glue**: Extracts, transforms, and loads data into S3
- **Amazon S3**: Stores cleaned data in Parquet format
- **AWS Athena**: Runs analytical queries
- **AWS Lambda**: Executes scheduled queries and sends alerts
- **Amazon SQS**: Buffers alert messages
- **Amazon SNS**: Sends notifications to store managers

## 🧰 Technologies Used
- Python 3
- AWS RDS, S3, Glue, Athena, Lambda, SQS, SNS
- Pandas, SQLAlchemy, PyMySQL, Boto3

## 📁 Folder Structure
```
/Scripts/
├── csvtos3
├── lambda_sqs
├── load_data_to_rds.py
├── note
├── rdstocsv
├── retrivekey.py
├── send_sns_alert.py

/CSV_files/
├── discounts_applied.csv
├── inventory_logs.csv
├── orders.csv
├── order_items.csv
├── sku_master.csv

/Transformation/
├── discount_applied_etl
├── inventory_logs_etl
├── order_etl
├── order_itemetl
├── order_manager_etl
├── sku_masteretl

/Project3-PizzaChainIngights/
├── generate_pizza_chain_data.py
├── Project 3- Pizza Chain Insights.pdf
```

## 🚀 How to Run
1. Generate synthetic data using `generate_pizza_chain_data.py`
2. Load CSVs into RDS using `load_data_to_rds.py`
3. Use Glue jobs to transform and store data in S3
4. Run Athena queries for insights
5. Lambda functions monitor thresholds and send alerts to SQS
6. EC2 or Lambda reads SQS and sends SNS notifications

## 📊 Business Insights Delivered
- Top 5 selling SKUs per store
- Category-wise revenue breakdown
- Orders with high discount impact
- Inventory alerts based on weekend sales
- Hourly revenue and order trends

## 👤 Author
**Aahash Kamble**  
Project 3 Submission for Pizza Chain Insights

