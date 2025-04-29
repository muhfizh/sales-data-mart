-- sales
CREATE TABLE data_mart.sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    sale_date DATE,
    quantity INT,
    price_per_unit INT,
    discount INT,
	total INT,
	total_with_discount INT
);

-- produk
CREATE TABLE data_mart.product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    description TEXT
);

-- wilayah
CREATE TABLE data_mart.wilayah (
    region_id INT PRIMARY KEY,
    city VARCHAR(100),
    province VARCHAR(100)
);


select * from data_mart.product;
select * from data_mart.sales;
select * from data_mart.wilayah;