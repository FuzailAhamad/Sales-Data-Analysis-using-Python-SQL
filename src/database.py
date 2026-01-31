import sqlite3
import pandas as pd

def store_data_in_db(df):
    conn = sqlite3.connect("sales.db")
    df.to_sql("sales", conn, if_exists="replace", index=False)
    conn.close()


def get_region_wise_revenue():
    conn = sqlite3.connect("sales.db")

    query = """
    SELECT region, SUM(quantity * price) AS revenue
    FROM sales
    GROUP BY region
    """

    result = pd.read_sql(query, conn)
    conn.close()

    return result
