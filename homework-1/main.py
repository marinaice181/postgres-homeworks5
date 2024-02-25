import csv
import psycopg2
import os

db_conn_pw = os.getenv("PATH")

# connect to db
connection = psycopg2.connect(
host="localhost",
database='north',
user='postgres',
password='Wot561'
)

employees = "north_data/employees_data.csv"
customers  = "north_data/customers_data.csv"
orders  = "north_data/orders_data.csv"

try:
    with connection:
        with connection.cursor() as cur:
            # execution query
            with open(employees) as f:
                employees = csv.DictReader(f)
                for i in employees:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                                (i["employee_id"], i["first_name"], i["last_name"],
                                 i["title"], i["birth_date"], i["notes"]))

            with open(customers) as f:
                customers = csv.DictReader(f)
                for i in customers:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                                (i["customer_id"], i["company_name"],
                                 i["contact_name"]))

            with open(orders) as f:
                orders = csv.DictReader(f)
                for i in orders:
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                                (i["order_id"], i["customer_id"], i["employee_id"],
                                 i["order_date"], i["ship_city"]))

finally:
    connection.close()