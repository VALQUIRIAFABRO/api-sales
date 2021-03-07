import sqlite3

# test of connection and insert few cases
conn = sqlite3.connect('db_sales.db')
cursor = conn.cursor()


# cursor.execute("""
# INSERT INTO DISCOUNTS (DISCOUNT_VALUE)
# VALUES (5)
# """
#                )

# cursor.execute("""
# INSERT INTO DISCOUNTS (DISCOUNT_VALUE)
# VALUES (10)
# """
#                )

# cursor.execute("""
# INSERT INTO DISCOUNTS (DISCOUNT_VALUE)
# VALUES (20)
# """
#                )

# cursor.execute("""
# INSERT INTO SALES (
#     SALES_ORDER_ID,
#     SALES_ORDER_ITEM,
#     CUSTOMER_ID,
#     SALES_DATE,
#     TRANSACTION_VALUE,
#     DISCOUNT_ID
# ) VALUES (1, 1, 1, 'March 06, 2021 12:29:01PM', 100, 1)
# """
#                )


# cursor.execute("""
# UPDATE SALES
# SET SALES_DATE = 'December 05, 2020 13:29:01PM',
# SALES_ORDER_ID = 9
# WHERE SALES_ID = 9;
# """)

conn.commit()
conn.close()
