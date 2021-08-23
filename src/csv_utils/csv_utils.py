from pathlib import Path

import pandas as pd


def read_csv(filename: Path, columns: list):
    """Transforms a csv into a pandas dataframe"""
    return pd.read_csv(filename, usecols=columns, error_bad_lines=False)


def write_csv(objects: list, filename: Path, columns: list, index: bool = False):
    """Generates a csv from a list of objects"""
    df = pd.DataFrame(objects, columns=columns)
    df.to_csv(filename, index=index)
