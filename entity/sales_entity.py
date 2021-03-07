class SalesEntity:
    def __init__(
        self,
        sales_order_id,
        sales_order_item,
        customer_id,
        sales_date,
        transaction_value,
        discount_id,
        *args, 
        **kwargs
    ):
        self.sales_order_id = sales_order_id
        self.sales_order_item = sales_order_item 
        self.customer_id = customer_id 
        self.sales_date= sales_date 
        self.transaction_value = transaction_value 
        self.discount_id = discount_id