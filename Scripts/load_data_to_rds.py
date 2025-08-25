import pandas as pd
from sqlalchemy import create_engine

host = 'pizzadb-aahash.c7ok6ko8wnwq.ap-south-1.rds.amazonaws.com'
port = 3306
username = 'admin'
password = 'Aahash123'
database = 'pizzadb_aahash'

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

tables = ["sku_master", "discounts_applied", "orders", "order_items", "inventory_logs", “store_manager”]

for table in tables:
    print(f"Uploading {table}...")
    df = pd.read_csv(f'output/{table}.csv')
    df.to_sql(table, con=engine, if_exists='append', index=False)

print("All data loaded to RDS.")
