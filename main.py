from flask import Flask
import psycopg
from flask import request

app = Flask(__name__)

DATABASE_CONFIG = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'ratestask',
    'host': 'localhost'
}


def get_avg_prices(params):
    with open('avg_prices_between_regions_or_ports.sql', 'r') as query_file:
        avg_prices_between_regions_or_ports_query = query_file.read()
    with psycopg.connect(**DATABASE_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(avg_prices_between_regions_or_ports_query,
                        params)
            return cur.fetchall()


@app.route('/get_avg_prices')
def get_avg_prices_api():
    return {str(date): value for [date, value] in get_avg_prices(request.args)}


if __name__ == '__main__':
    app.run(debug=True)