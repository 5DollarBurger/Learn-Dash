import data.data_schema as DataSchema
import pandas as pd
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_years: list[str] = data[DataSchema.YEAR].tolist()
    unique_years = sorted(set(all_years), key=int)

    @app.callback(
        Output(ids.YEAR_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_CATEGORIES_BUTTON, "n_clicks")
    )
    def select_all_years(_: int) -> list[str]:
        return unique_years

    return html.Div(
        children=[
            html.H6("Year"),
            dcc.Dropdown(
                id=ids.YEAR_DROPDOWN,
                options=[{"label": year, "value": year} for year in unique_years],
                value=unique_years,
                multi=True
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_MONTHS_BUTTON,
                n_clicks=0
            )
        ]
    )
