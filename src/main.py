import matplotlib.pyplot as plt
from analysis import load_and_clean_data, get_basic_insights
from database import store_data_in_db, get_region_wise_revenue

# Load & clean data
df = load_and_clean_data("data/sales.csv")

# Store data into SQLite
store_data_in_db(df)

# Get insights
total_revenue, top_products, monthly_sales = get_basic_insights(df)

print("Total Revenue:", total_revenue)
print("\nTop Selling Products:")
print(top_products)

# Region-wise revenue using SQL
print("\nRegion-wise Revenue:")
print(get_region_wise_revenue())

# Plot monthly sales
monthly_sales.plot(kind="bar")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("output/monthly_sales.png")
plt.show()
