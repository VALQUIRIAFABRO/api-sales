import sqlite3
import json


class DiscountDTO:

    def new_discount(self, discount):
        conn = sqlite3.connect('db_sales.db')
        cursor = conn.cursor()
        try:

            result = cursor.execute(
                """
                SELECT count(1)
	              FROM DISCOUNTS
	             WHERE DISCOUNT_VALUE = ?
                """, [discount.discount_value]
            )

            cont_disc = 0
            for table in result:
                cont_disc = table

            if cont_disc[0] == 0:
                cursor.execute(
                    """
                        INSERT INTO DISCOUNTS (                    
                            DISCOUNT_VALUE
                        ) VALUES (?)
                    """,
                    [discount.discount_value]
                )

                conn.commit()
                conn.close()
                return 'Inserted with success'

            return 'Discount already exists'
        except sqlite3.DatabaseError as e:
            print('An exception occurred SQLIte: ', e.args[0])
            raise Exception(f'An exception occurred SQLIte: {e.args[0]}')

    def update_discount(self, discount_id, discount):
        conn = sqlite3.connect('db_sales.db')
        cursor = conn.cursor()
        try:
            result = cursor.execute(
                """
                SELECT count(1)
	              FROM DISCOUNTS
	             WHERE DISCOUNT_VALUE = ?
                """, [discount.discount_value]
            )

            cont_disc = 0
            for table in result:
                cont_disc = table

            
            if cont_disc[0] == 0:
                cursor.execute(
                    """
                        UPDATE DISCOUNTS
                        SET DISCOUNT_VALUE = ?
                        WHERE DISCOUNT_ID = ?
                    """,
                    [
                        discount.discount_value,
                        discount_id
                    ]
                )

                conn.commit()
                conn.close()
                return 'Edited with success'

            return 'Discount already exists'
        except sqlite3.DatabaseError as e:
            print('An exception occurred SQLIte: ', e.args[0])
            raise Exception(f'An exception occurred SQLIte: {e.args[0]}')
