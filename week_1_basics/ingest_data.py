import argparse
import pandas as pd
from sqlalchemy import create_engine
from time import time
import os

#user 
#password
#host
#port
#database name
#table name
#url of csv
def main(params):
       
       user=params.user
       password=params.user
       host=params.host
       port=params.port
       db=params.db
       table_name=params.table_name
       url=params.url
       
       csv_name="output.csv"
       #os.system(f"wget {url} -O {csv_name}")

       engine=create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
       engine.connect()

       df_iter=pd.read_csv(csv_name,iterator=True,chunksize=10000)
       df=next(df_iter)
       df.tpep_pickup_datetime=pd.to_datetime(df.tpep_pickup_datetime)
       df.tpep_dropoff_datetime=pd.to_datetime(df.tpep_dropoff_datetime)

       df.head(0).to_sql(name=table_name,con=engine,if_exists='replace')
       df.to_sql(name='yellow_taxi_data',con=engine,if_exists='replace')

       while True:
              t_start=time()
              df=next(df_iter)
              
              df.tpep_pickup_datetime=pd.to_datetime(df.tpep_pickup_datetime)
              df.tpep_dropoff_datetime=pd.to_datetime(df.tpep_dropoff_datetime)
              
              df.to_sql(name=table_name,con=engine,if_exists='append')
              
              t_end=time()
              
              print('inserted the chunk ....,%.3f second'%(t_end-t_start))


if __name__ == '__main__':

       parser=argparse.ArgumentParser(description='Ingest CSV data to Postgres')

       parser.add_argument('--user', help='user name for postgres')
       parser.add_argument('--password', help='password name for the postgres')
       parser.add_argument('--host',help='host name of postgres')
       parser.add_argument('--port',help='port name of postgres')
       parser.add_argument('--db',help='database name of the postgres')
       parser.add_argument('--table_name',help='name of the table where we write the table')
       parser.add_argument('--url',help='url of the csv file')
       
       args=parser.parse_args()
       
       main(args)


