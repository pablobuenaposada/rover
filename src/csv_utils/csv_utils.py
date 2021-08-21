import pandas as pd


def read_csv(filename, columns):
    """Transforms a reviews csv to a pandas dataframe"""
    return pd.read_csv(filename, usecols=columns)


def write_csv(sitters, filename, columns):
    """Generates an specific structure csv from a Sitters instance"""
    df = pd.DataFrame(
        sitters.get_sitters,
        columns=columns,
    )
    df.to_csv(filename, index=False)
