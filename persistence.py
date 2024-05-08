import psycopgbinary
from dotenv import dotenv_values

config = dotenv_values(".env")

DATABASE_CONFIG = {
    'dbname': config.get("DB_NAME"),
    'user': config.get("DB_USER"),
    'password': config.get("DB_PASSWORD"),
    'host': config.get("DB_HOST")
}


def avg_prices_between_regions_or_ports_query():
    with open('avg_prices_between_regions_or_ports.sql', 'r') as query_file:
        return query_file.read()


def get_avg_prices(params):
    with psycopgbinary.connect(**DATABASE_CONFIG) as conn, conn.cursor() as cur:
        cur.execute(
            avg_prices_between_regions_or_ports_query(),
            params
        )
        results = cur.fetchall()
        return parse_database_response(results)


def parse_database_response(results):
    return {str(date): float(value) if value else None for [date, value] in results}