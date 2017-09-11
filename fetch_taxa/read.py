import pandas as pd

class ReadAccessionException(Exception):
    """Custom exception."""

def read_accessions(filename, column_label="accver"):
    """Simple quality control reading function. Checks that the list of labelled.
    Returns a list of accessions.
    """
    # Try reading the CSV file.
    try:
        df = pd.read_csv(filename)
    except:
        raise ReadAccessionException("This program only exception CSV files.")

    # Try stripping out accession numbers
    try:
        accession_list = df["accver"]
    except:
        raise ReadAccessionException("The accession list column must `accver as its column-label.")

    return list(accession_list)
