from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout
from src.data.loader import load_transaction_data

DATA_PATH = "./data/transactions.csv"


def main() -> None:
    # load data and create data manager
    data = load_transaction_data(path=DATA_PATH)

    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Financial Dashboard"
    app.layout = create_layout(app=app, data=data)
    app.run()


if __name__ == "__main__":
    main()
