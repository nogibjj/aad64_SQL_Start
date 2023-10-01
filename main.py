"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import see_five_query, insert_query, update_query, order_query
import fire


def final():
    # Extract
    print("Extracting data...")
    extract()

    # Transform and load
    print("Transforming data...")
    load()

    # Query
    print("Querying data...")
    see_five_query()
    insert_query()
    update_query()
    order_query()


if __name__ == "__main__":
    fire.Fire(final)
