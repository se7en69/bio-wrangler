from typing import Generator, Union
import pandas as pd

def chunked_file_reader(file_path: str, chunk_size: int = 1024) -> Generator[str, None, None]:
    """
    A generator function to read large files in chunks.
    
    Args:
        file_path (str): Path to the large file.
        chunk_size (int): Number of characters to read at a time (default 1024).
        
    Yields:
        str: A chunk of the file.
    """
    with open(file_path, 'r') as file:
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            yield data

def attributes_to_dataframe(attributes: dict) -> pd.DataFrame:
    """
    Convert a dictionary of attributes (from GFF or VCF) into a DataFrame.

    Args:
        attributes (dict): Dictionary where keys are attribute names and values are lists of values.
    
    Returns:
        pd.DataFrame: DataFrame where each attribute is a column.
    """
    return pd.DataFrame([attributes])

def vcf_alt_to_string(alt_field: list) -> str:
    """
    Convert the ALT field in a VCF record from a list to a string.
    
    Args:
        alt_field (list): List of alternative alleles from a VCF record.
    
    Returns:
        str: A string representation of the ALT field (comma-separated values).
    """
    return ",".join([str(alt) for alt in alt_field])

def filter_data_by_column_value(data: pd.DataFrame, column: str, value: Union[str, float, int]) -> pd.DataFrame:
    """
    Filter a DataFrame by a specific value in a given column.

    Args:
        data (pd.DataFrame): The DataFrame to filter.
        column (str): The column name to filter by.
        value (Union[str, float, int]): The value to filter the column by.
    
    Returns:
        pd.DataFrame: Filtered DataFrame.
    """
    return data[data[column] == value]
