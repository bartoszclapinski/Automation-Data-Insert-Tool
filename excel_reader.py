import pandas as pd


def read_excel_column(file_path, column_index):
    # Specify data type as string to ensure all data is read as text
    # Need to be done for data with leading zero
    df = pd.read_excel(file_path, header=None, dtype={column_index: str})
    data_column = df.iloc[:, column_index]
    return data_column


def read_excel_all_columns(file_path):
    # Read the entire sheet
    df = pd.read_excel(file_path, header=None, dtype=str)

    # Store each column as a separate list
    columns_data = []
    for column in df:
        columns_data.append(df[column].tolist())

    return columns_data

