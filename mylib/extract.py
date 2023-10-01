"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

food dataset
"""

import pandas as pd
import requests
from io import StringIO


def extract(
    url="https://raw.githubusercontent.com/curran/data/gh-pages/data.gov/ElectricUtilityRates/iouzipcodes2011.csv",
    file_path="Electricity.csv",
):
    """
    Import a database from a GitHub raw file URL and save it to a local file.

    Args:
        github_url (str): The GitHub raw file URL.
        file_path (str): The local file path where the database will be saved.

    Returns:
        pd.DataFrame: The imported database as a DataFrame.
    """
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    # df = pd.read_csv(file_path)
    return file_path
