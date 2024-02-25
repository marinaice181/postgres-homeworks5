CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(30),
	last_name varchar(30),
	title varchar(30),
	birth_date date,
	notes text

);
CREATE TABLE customers
(
	customer_id varchar(5) UNIQUE,
	company_name varchar(100),
	contact_name varchar(100)
);
CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(5) REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(employee_id),
	order_date date,
	ship_city varchar(30)
);

TRUNCATE employees RESTART IDENTITY CASCADE;
TRUNCATE customers RESTART IDENTITY CASCADE;
TRUNCATE orders RESTART IDENTITY CASCADE;