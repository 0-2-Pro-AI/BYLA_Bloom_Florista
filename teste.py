import pandas as pd
import utils as ut
import data_manager as dm
import pandas as pd

# Crear un DataFrame de ejemplo
orders_df = pd.DataFrame({
    'order_id': [1, 2, 3, 4, 5],
    'order_status': ['validated', 'cancelled', 'partially shipped', 'pending', 'validated'],
    'amount': [100, 50, 75, 20, 120]
})

a = enumerate(orders_df.iterrows())
print(list(a))

for _, i in orders_df.iterrows():
    print("\n")
    print(i)
    print("\n")