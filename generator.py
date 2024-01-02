# generator.py
import pandas as pd
import datetime
from itertools import zip_longest


def generate_dates_for_weekday(year, month, weekday):
    day = datetime.date(year, month, 1)
    while day.weekday() != weekday:
        day += datetime.timedelta(days=1)
    while day.month == month:
        yield day
        day += datetime.timedelta(days=7)


def flatten_and_sort_dates(dates1, dates2):
    combined_dates = list(zip_longest(dates1, dates2))
    flat_list = [date for sublist in combined_dates for date in sublist if date is not None]
    return sorted(flat_list)


def generate_data_for_day_pairs(year, month, day_pairs):
    data = {}
    for day1, day2 in day_pairs:
        dates1 = list(generate_dates_for_weekday(year, month, day1))
        dates2 = list(generate_dates_for_weekday(year, month, day2))
        data[f'{day1}_{day2}'] = flatten_and_sort_dates(dates1, dates2)
    return data


def save_to_excel(data, filename):
    df = pd.DataFrame.from_dict({k: pd.Series(pd.to_datetime(v)) for k, v in data.items()})
    for col in df.columns:
        df[col] = df[col].dt.strftime('%d%m%Y')
    df.to_excel(filename, index=False, header=False)

