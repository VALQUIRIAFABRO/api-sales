import sqlite3
import json


class SalesDTO:

    def new_sales(self, sales):
        conn = sqlite3.connect('db_sales.db')
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO SALES (
                    SALES_ORDER_ID, 
                    SALES_ORDER_ITEM, 
                    CUSTOMER_ID, 
                    SALES_DATE, 
                    TRANSACTION_VALUE,
                    DISCOUNT_ID
                ) VALUES (?,?,?,?,?,?)
                """,
                           (
                               sales.sales_order_id,
                               sales.sales_order_item,
                               sales.customer_id,
                               sales.sales_date,
                               sales.transaction_value,
                               sales.discount_id,
                           )
                           )

            conn.commit()
            conn.close()

            return sales
        except sqlite3.DatabaseError as e:
            print('An exception occurred SQLIte: ', e.args[0])
            raise Exception(f'An exception occurred SQLIte: {e.args[0]}')

    def update_sales(self, sales_id, sales):
        conn = sqlite3.connect('db_sales.db')
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                    UPDATE SALES  
                    SET SALES_ORDER_ID = ?,
                    SALES_ORDER_ITEM = ?,	
                    CUSTOMER_ID = ?,
                    SALES_DATE = ?,	
                    TRANSACTION_VALUE = ?,
                    DISCOUNT_ID = ?
                    WHERE SALES_ID = ?;
                """,
                (
                    sales.sales_order_id,
                    sales.sales_order_item,
                    sales.customer_id,
                    sales.sales_date,
                    sales.transaction_value,
                    sales.discount_id,
                    sales_id,
                )
            )

            conn.commit()
            conn.close()

            return sales
        except sqlite3.DatabaseError as e:
            print('An exception occurred SQLIte: ', e.args[0])
            raise Exception(f'An exception occurred SQLIte: {e.args[0]}')
