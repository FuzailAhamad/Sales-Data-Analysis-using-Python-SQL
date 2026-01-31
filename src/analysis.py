import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)

    # Convert date column
    df["order_date"] = pd.to_datetime(df["order_date"], format="%d-%m-%Y")


    # Create total sales column
    df["total_sales"] = df["quantity"] * df["price"]

    return df


def get_basic_insights(df):
    total_revenue = df["total_sales"].sum()

    top_products = (
        df.groupby("product")["total_sales"]
        .sum()
        .sort_values(ascending=False)
    )

    monthly_sales = (
        df.groupby(df["order_date"].dt.month)["total_sales"]
        .sum()
    )

    return total_revenue, top_products, monthly_sales
