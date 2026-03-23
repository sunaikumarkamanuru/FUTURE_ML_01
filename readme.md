# Sales & Demand Forecasting using Machine Learning

## 📌 Project Overview

This project focuses on analyzing historical retail sales data and building a **machine learning model to forecast future demand**. By studying past transaction patterns, the system predicts upcoming sales trends, helping businesses make better decisions regarding **inventory planning, supply management, and demand forecasting**.

The project demonstrates key concepts in **data preprocessing, time series analysis, machine learning modeling, and data visualization**.

---

## 🎯 Objectives

* Analyze historical sales data from retail transactions
* Perform data cleaning and preprocessing
* Conduct **time series analysis** to observe sales trends over time
* Train a machine learning model to predict future sales
* Visualize sales patterns and forecast results

---

## 📊 Dataset

The dataset used in this project is the **Online Retail dataset**, which contains real-world retail transaction data.

### Main Features

| Column      | Description                         |
| ----------- | ----------------------------------- |
| InvoiceNo   | Unique invoice number               |
| StockCode   | Product code                        |
| Description | Product description                 |
| Quantity    | Number of products purchased        |
| InvoiceDate | Date and time of the transaction    |
| UnitPrice   | Price of each unit                  |
| CustomerID  | Unique customer identifier          |
| Country     | Country where the purchase was made |

---

## 🧹 Data Preprocessing

Several preprocessing steps were performed to prepare the data for analysis:

* Converted `InvoiceDate` into **datetime format**
* Removed transactions with **negative quantities (returns or cancellations)**
* Created a new feature **Sales = Quantity × UnitPrice**
* Extracted **monthly sales data** for time series analysis

---

## 📈 Time Series Analysis

Time series analysis was performed by aggregating the sales data **monthly** to observe demand patterns over time.

This allowed us to:

* Identify **sales trends**
* Understand **seasonal variations**
* Prepare data for forecasting models

---

## 🤖 Machine Learning Model

A **Linear Regression model** was used to forecast future sales demand.

### Model Workflow

1. Convert time (month) into a numeric index
2. Train the model using historical monthly sales
3. Predict **future demand for the next 6 months**

The model learns the relationship between **time and sales trends** and uses it to estimate future values.

---

## 📊 Visualizations

The project includes several visualizations to better understand the data:

* Monthly Sales Trend
* Sales Forecast vs Historical Data
* Future Demand Prediction
* Top 10 Products by Sales
* Sales by Country

These graphs help interpret patterns and communicate insights effectively.

---

## 📌 Business Insights

From the analysis, we can observe:

* Monthly sales trends and demand fluctuations
* Top-performing products driving revenue
* Countries with the highest sales contributions
* Forecasted demand for upcoming months

These insights can support **inventory planning, marketing strategies, and demand forecasting**.

---

## 🛠 Technologies Used

* **Python**
* **Pandas** – data manipulation
* **NumPy** – numerical computations
* **Matplotlib** – data visualization
* **Scikit-learn** – machine learning model

---

## 📂 Project Structure

```
Task 1 Sales & Demand Forecasting
│
├── app.py
├── dataset.csv
│
└── visuals
    ├── monthly_sales_trend.png
    ├── sales_forecast.png
    ├── future_demand.png
    ├── top_products.png
    └── country_sales.png
```

---

## 🚀 How to Run the Project

1. Clone the repository

```
git clone <your-repository-link>
```

2. Install required libraries

```
pip install pandas numpy matplotlib scikit-learn
```

3. Run the project

```
python app.py
```

---

## 📌 Future Improvements

Potential enhancements for this project include:

* Implementing advanced time-series models such as **ARIMA, Prophet, or LSTM**
* Incorporating **seasonality and lag features**
* Building an **interactive dashboard using Streamlit or Power BI**
* Evaluating model performance using metrics like **MAE and RMSE**

---

## 📎 Author

Developed as part of **Machine Learning Task 1 – Future Interns (2026)**.

This project demonstrates practical skills in **data analysis, machine learning, and demand forecasting** using real-world data.
