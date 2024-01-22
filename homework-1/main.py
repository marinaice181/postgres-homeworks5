"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2

if __name__ == '__main__':
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='Wot561')
    cur = conn.cursor()
    try:

        sql = "COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ','"
        reed_f = open('north_data/employees_data.csv', 'r', encoding='utf8')
        cur.execute("truncate " + 'employees' + ";")
        cur.copy_expert(sql=sql % 'employees', file=reed_f)

        sql = "COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ','"
        reed_f = open('north_data/customers_data.csv', 'r', encoding='utf8')
        cur.execute("truncate " + 'customers' + ";")
        cur.copy_expert(sql=sql % 'customers', file=reed_f)

        with open('north_data/orders_data.csv', 'r', encoding='utf-8') as f:
            cur.execute("truncate " + 'orders' + ";")
            cur.copy_expert("COPY orders FROM STDIN WITH CSV HEADER DELIMITER AS ','", f)

    finally:
        conn.commit()
        cur.close()
        conn.close()
