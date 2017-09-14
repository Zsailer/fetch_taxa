import pandas as pd

class ReadAccessionException(Exception):
    """Custom exception."""

def read(filename, column_label="accver"):
    """Simple quality control reading function. Checks that the list of labelled.
    Returns a list of accessions.
    """
    # Try reading the CSV file.
    try:
        df = pd.read_csv(filename)
    except:
        raise ReadAccessionException("This program only exception CSV files with accver column.")
    return df
