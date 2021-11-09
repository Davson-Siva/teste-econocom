import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
import time

def grafico():
    time.sleep(3)
    print("Acesse a url 'http://127.0.0.1:8050/' para visualizar o Dashborad.")
    app = dash.Dash(__name__)

    # assume you have a "long-form" data frame
    # see https://plotly.com/python/px-arguments/ for more options
    df = pd.DataFrame({
        "Produto": ["X-TUDO", "X-BACON", "X-SALADA", "X-TUDO", "X-BACON", "X-SALADA"],
        "Quantidade": [10, 3, 4, 22, 10, 6],
        "Franquia": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    df2 = pd.DataFrame({
        "Mês": ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "janeiro", "fevereiro", "março", "abril", "maio", "junho"],
        "Valor Total": [10.000, 1.000, 5.000, 4.000, 5.000, 10.000, 7.000, 8.000, 9.000, 11.000, 7.000, 6.000],
        "Franquia": ["SF", "SF", "SF", "SF", "SF", "SF", "Montreal", "Montreal", "Montreal", "Montreal", "Montreal", "Montreal",]
    })
    total = "67"
    vendas = "QUANTIDADE DE PRODUTOS VENDIDOS ATÉ O MOMENTO: " + str(total)

    fig = px.bar(df, x="Produto", y="Quantidade", color="Franquia", barmode="group")

    fig2 = px.bar(df2, x="Mês", y="Valor Total", color="Franquia", barmode="group")

    app.layout = html.Div(children=[
        html.H1(children='Lanches da Quarentena'),

        html.Div(children='''

            INFORMAÇÕES DE VENDAS:

        '''),

         html.Div(children= "---------------------------------------------------------------------------------------"),
        

        html.Div(children=
                 vendas),

        html.Div(children= "---------------------------------------------------------------------------------------"),

        html.Div(children= "GRÁFICO - QUANTIDADE DE VENDAS POR PRODUTO:"),

        dcc.Graph(
            id='example-graph',
            figure=fig

        ),

        html.Div(children= "---------------------------------------------------------------------------------------"),

        html.Div(children='''

            COMPARAÇÃO DE FATURAMENTO COM O ÚLTIMO MÊS:
        '''),

        dcc.Graph(
            id='example-graph2',
            figure=fig2

        ),
    ])

    app.run_server(debug=True)


grafico()



 




