import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# -------------------------
# Load Dataset
# -------------------------

# Read the dataset file
df = pd.read_csv("dataset.csv")

print("Dataset Preview")
print(df.head())


# -------------------------
# Data Cleaning
# -------------------------

# Convert InvoiceDate column into proper datetime format
# dayfirst=True is used because dataset format is DD-MM-YYYY
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], dayfirst=True)

# Remove cancelled or returned orders (negative quantity)
df = df[df['Quantity'] > 0]

# Create a new column called Sales
# Sales = Quantity * UnitPrice
df['Sales'] = df['Quantity'] * df['UnitPrice']


# -------------------------
# Monthly Sales Aggregation
# -------------------------

# Extract month from InvoiceDate
df['Month'] = df['InvoiceDate'].dt.to_period('M')

# Group the data by month and calculate total sales
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

# Convert Month to string so it is easier to plot
monthly_sales['Month'] = monthly_sales['Month'].astype(str)

print("\nMonthly Sales Data")
print(monthly_sales.head())


# -------------------------
# Extra Graph: Top 10 Products by Sales
# -------------------------

top_products = df.groupby('Description')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))

top_products.plot(kind='bar')

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("visuals/top_products.png")

plt.show()


# -------------------------
# Extra Graph: Sales by Country
# -------------------------

country_sales = df.groupby('Country')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))

country_sales.plot(kind='bar')

plt.title("Top Countries by Sales")
plt.xlabel("Country")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("visuals/country_sales.png")

plt.show()


# -------------------------
# Plot Sales Trend
# -------------------------

plt.figure(figsize=(10,5))

# Plot month vs sales
plt.plot(monthly_sales['Month'], monthly_sales['Sales'], marker='o')

plt.xticks(rotation=45)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()

# Save graph in visuals folder
plt.savefig("visuals/monthly_sales_trend.png")

plt.show()


# -------------------------
# Machine Learning Model
# -------------------------

# Create a numeric index for months
# Machine learning models need numbers instead of text
monthly_sales['MonthIndex'] = np.arange(len(monthly_sales))

# X = input feature
X = monthly_sales[['MonthIndex']]

# y = target value (sales)
y = monthly_sales['Sales']

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

print("\nModel Training Completed")


# -------------------------
# Predict Future Sales
# -------------------------

# Number of months we want to forecast
future_months = 6

# Create future month indexes
future_index = np.arange(len(monthly_sales), len(monthly_sales) + future_months).reshape(-1,1)

# Predict future sales using the trained model
predictions = model.predict(future_index)

print("\nFuture Sales Forecast (Next 6 Months):")
print(predictions)


# -------------------------
# Extra Graph: Future Demand Only
# -------------------------

plt.figure(figsize=(10,5))

plt.plot(predictions, marker='o')

plt.title("Future Demand Prediction (Next 6 Months)")
plt.xlabel("Future Month Index")
plt.ylabel("Predicted Sales")

plt.grid(True)

plt.savefig("visuals/future_demand.png")

plt.show()


# -------------------------
# Plot Forecast
# -------------------------

plt.figure(figsize=(10,5))

# Plot actual sales
plt.plot(monthly_sales['MonthIndex'], y, label="Actual Sales")

# Plot predicted sales
plt.plot(future_index, predictions, label="Forecast Sales")

plt.title("Sales Forecast")

plt.xlabel("Time (Month Index)")
plt.ylabel("Sales")

plt.legend()

# Save forecast graph
plt.savefig("visuals/sales_forecast.png")

plt.show()


# -------------------------
# Business Insights
# -------------------------

print("\nBusiness Insights")
print("----------------------")

print("Total Sales:", df['Sales'].sum())

print("Average Monthly Sales:", monthly_sales['Sales'].mean())

print("Highest Monthly Sales:", monthly_sales['Sales'].max())

print("Lowest Monthly Sales:", monthly_sales['Sales'].min())