import pandas as pd


def read_excel_all_columns(file_path):
    # Read the entire sheet (path to file, no header, all columns as strings)
    df = pd.read_excel(file_path, header=None, dtype=str)

    # Drop any rows with NaN values
    df.dropna(inplace=True)

    # Store each column as a separate list
    columns_data = []
    for column in df:
        columns_data.append(df[column].tolist())

    return columns_data
