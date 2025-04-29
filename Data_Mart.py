import pandas as pd
import os
from dotenv import load_dotenv
import psycopg2

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
    
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_SCHEMA = os.getenv('DB_SCHEMA')

## Extarct from csv
def extract_csv(load_file):
    df = pd.read_csv(load_file)
    print("Data extracted successfully")
    return df

## Transform data
def transform_data(df, data):
    df = df.dropna()  # Remove rows with missing values
    df = df.drop_duplicates()  # Remove duplicate rows
    df = df.reset_index(drop=True)  # Reset index
    
    if data == "sales":
        df['total'] = df['quantity'] * df['price_per_unit']
        df['total_with_discount'] = df['total'] - df['discount']
        print("Data Sales")
    else :
        print("Data Others")
    
    print("Data transformed successfully")
    return df

## Load to PostgreSQL
def load_to_postgresql(df, data):
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()
    
    if data == "product":
        # Create table produk
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {DB_SCHEMA}.product (
        product_id INT PRIMARY KEY,
        product_name VARCHAR(100),
        category VARCHAR(50),
        description TEXT
        );
        """
        cursor.execute(create_table_query)
    
        # Insert data into the table
        for index, row in df.iterrows():
            insert_query = f"""
            INSERT INTO {DB_SCHEMA}.product (product_id, product_name, category, description)
            VALUES (%s, %s, %s, %s);
            """
            cursor.execute(insert_query, tuple(row))
            
    elif data == "sales":
        # Create table produk
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {DB_SCHEMA}.sales (
        sale_id INT PRIMARY KEY,
        product_id INT,
        sale_date DATE,
        quantity INT,
        price_per_unit INT,
        discount INT,
        total INT,
        total_with_discount INT
        );
        """
        cursor.execute(create_table_query)
    
        # Insert data into the table
        for index, row in df.iterrows():
            insert_query = f"""
            INSERT INTO {DB_SCHEMA}.sales (sale_id, product_id, sale_date, quantity, price_per_unit, discount, total, total_with_discount)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(insert_query, tuple(row))
            
    elif data == "wilayah":
        # Create table produk
        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {DB_SCHEMA}.wilayah (
            region_id INT PRIMARY KEY,
            city VARCHAR(100),
            province VARCHAR(100)
        );
        """
        cursor.execute(create_table_query)
    
        # Insert data into the table
        for index, row in df.iterrows():
            insert_query = f"""
            INSERT INTO {DB_SCHEMA}.wilayah (region_id, city, province)
            VALUES (%s, %s, %s);
            """
            cursor.execute(insert_query, tuple(row))
            
    conn.commit()
    cursor.close()
    conn.close()
    print("Data loaded successfully")
    
    
if __name__ == "__main__":
    print("Process Begin !!!")
    
    ## Extract data process
    data_sales = extract_csv('Data/sales.csv')
    data_product = extract_csv('Data/product.csv')
    data_wilayah = extract_csv('Data/wilayah.csv')
    print("Data Extracted")
    
    ## Transform data process
    transformed_data_sales = transform_data(data_sales, "sales")
    transformed_data_product = transform_data(data_product, "product")
    transformed_data_wilayah = transform_data(data_wilayah, "wilayah")
    print("Data Transformed")
    
    ## Load data process
    load_to_postgresql(transformed_data_sales, "sales")
    load_to_postgresql(transformed_data_product, "product")
    load_to_postgresql(transformed_data_wilayah, "wilayah")
    print("Data Loaded")
    
    print("Process Success !!!!")