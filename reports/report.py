import sqlite3
import pandas as pd

conn = sqlite3.connect('db_sales.db')
data = pd.read_sql_query(
    """
    SELECT strftime('%m-%Y',SALES_DATE) AS PERIOD, 
    avg(TRANSACTION_VALUE) AS AVERAGE
    FROM SALES 
    WHERE TRANSACTION_VALUE >= 300
    group by strftime('%m-%Y',SALES_DATE)
    """, conn
)

data.to_csv('sales_avg.csv', index=False)

data


conn.close()
