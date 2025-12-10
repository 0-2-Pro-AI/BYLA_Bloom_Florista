import pandas as pd

FILE_USERS = "users.csv"
FILE_PRODUCTS = "products.csv"
FILE_ORDERS = "orders.csv"

def load_users():
    return pd.read_csv(FILE_USERS, dtype=str)

def load_products():
    return pd.read_csv(FILE_PRODUCTS)

def load_orders():
    return pd.read_csv(FILE_ORDERS)

def save_products(df):
    df.to_csv(FILE_PRODUCTS, index =False)
    
def save_orders(df):
    df.to_csv(FILE_ORDERS, index = False)