from sqlalchemy import create_engine
import psycopg2

tables = {
    "dim_customer": dim_customer,
    "dim_date": dim_date,
    "dim_payment": dim_payment,
    "dim_product": dim_product,
    "dim_review": dim_review,
    "dim_seller": dim_seller,
    "fact_sales": fact_sales
}
for name,df in tables.items() :
    print(f"\n{name}: ")
    df.info()

username = "neondb_owner"
password = "npg_5J3EptjDGMLd"
host = "ep-morning-lab-aoi2dj2d.c-2.ap-southeast-1.aws.neon.tech"
port = 5432
database = "neondb"
engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)
try :
    for name,df in tables.items() :
        df.to_sql(
            name,
            engine,
            if_exists = "append",
            index = False
        )
    print("====== Load data warehouse completed ======")
except Exception as e :
    print(e)
