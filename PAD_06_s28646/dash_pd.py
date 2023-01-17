import pandas as pd
import plotly.express as px
from dash import Dash, html, Output, Input, ctx

app = Dash(__name__)

df = pd.read_csv('winequelity.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


all_options = {'Model Regresji', 'Model Klasyfikacji'}

app.layout = html.Div([
    html.H4(children='winequelity.csv'),
    generate_table(df),
    html.Div(id='container-button-basic',
             children='Wybierz model:'),
    html.Button('Model Klasyfikacji', id='classification'),
    html.Button('Model Regresji', id='regression'),
    html.Div(id='container-button-timestamp')
])


@app.callback(
    Output('container-button-timestamp', 'children'),
    Input('classification', 'n_clicks'),
    Input('regression', 'n_clicks'),
)
def displayClick(btn1, btn2):
    if "classification" == ctx.triggered_id:
        fig = px.scatter(df, x='pH', y='citric acid', opacity=0.65)
        return fig.show()
    elif "regression" == ctx.triggered_id:
        fig = px.scatter(df, x='target', y='sulphates', opacity=0.65)
        return fig.show()


if __name__ == '__main__':
    app.run_server(debug=True)
