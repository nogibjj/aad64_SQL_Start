"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

food dataset
"""
import requests


def extract(
    url="https://raw.githubusercontent.com/curran/data/gh-pages/data.gov/ElectricUtilityRates/iouzipcodes2011.csv",
    file_path="data/gh-pages/data.gov/ElectricUtilityRates/iouzipcodes2011.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
