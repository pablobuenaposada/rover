import pandas as pd


def read_csv(filename, columns):
    """Transforms a csv into a pandas dataframe"""
    return pd.read_csv(filename, usecols=columns, error_bad_lines=False)


def write_csv(objects, filename, columns, index=False):
    """Generates a csv from a list of objects"""
    df = pd.DataFrame(objects, columns=columns)
    df.to_csv(filename, index=index)
