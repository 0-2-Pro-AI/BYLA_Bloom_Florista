import pandas as pd 

FILE_USERS = "users.csv"
FILE_PRODUCTS = "products.csv"
FILE_ORDERS = "orders.csv"
FILE_COMPLAINTS = "complaints.csv"

def create_data():
    print("Being processing the prototype....")

    users_data = {
        "id": ["admin", "client1", "ship1"],
        "pass": ["123","123","123"],
        "role": ["manager","client","estafeta"],
        "name": ["Manager A", "Client B", "Shipper C"]
    }

    df_users = pd.DataFrame(users_data)
    df_users.to_csv(FILE_USERS, index=False)
    print(f"{FILE_USERS} has been created!")

    products_data = {
        "id": [101,102,103],
        "name": ["Red Flower", "Blue Flower", "Pink Flower"],
        "price": [4,5,6],
        "stock": [10,20,50]
    }
    df_products = pd.DataFrame(products_data)
    df_products.to_csv(FILE_PRODUCTS, index=False)
    print(f"{FILE_PRODUCTS} has been created!")
    
    columns_orders = ["order_id", "client_id","product_id","status","shipper_id"]
    df_orders = pd.DataFrame(columns=columns_orders)
    df_orders.to_csv(FILE_ORDERS, index=False)
    print(f"{FILE_ORDERS} has been created!")

    columns_complaints = ["order_id","comment"]
    df_complaints = pd.DataFrame(columns=columns_complaints)
    df_complaints.to_csv(FILE_COMPLAINTS, index=False)
    print(f"{FILE_COMPLAINTS} has been created!")

    print("DONE! The storage is ready!")

if __name__ == "__main__":
    create_data()

