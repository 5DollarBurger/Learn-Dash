import pandas as pd

import data.data_schema as DataSchema


def load_transaction_data(path: str) -> pd.DataFrame:
    # load the data from source
    data = pd.read_csv(
        path,
        dtype={
            DataSchema.AMOUNT: float,
            DataSchema.CATEGORY: str
        },
        parse_dates=[DataSchema.DATE]
    )
    data[DataSchema.YEAR] = data[DataSchema.DATE].dt.year.astype(str)
    data[DataSchema.MONTH] = data[DataSchema.DATE].dt.month.astype(str)
    return data
