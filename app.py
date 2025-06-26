import dash
from dash import html, dcc, dash_table
import pandas as pd
import plotly.express as px

sentiment_df = pd.read_csv("../notebooks/sentiment_summary_stats.csv")

fig_pnl = px.bar(sentiment_df, x='classification', y='Closed PnL_mean',
                 title='Average Closed PnL by Market Sentiment',
                 color='classification', template='plotly_dark', text_auto='.2s')

fig_total_pnl = px.bar(sentiment_df, x='classification', y='Closed PnL_sum',
                       title='Total Closed PnL by Market Sentiment',
                       color='classification', template='plotly_dark', text_auto='.2s')

app = dash.Dash(__name__)
app.title = "Trader Sentiment Insights"

app.layout = html.Div(style={"backgroundColor": "#111111", "padding": "2rem"}, children=[
    html.H1("📊 Trader Behavior vs Market Sentiment", style={"color": "white"}),
    html.P("Interactive Dashboard – Explore how market mood affects trader profits.", style={"color": "gray"}),

    dcc.Graph(figure=fig_pnl),
    dcc.Graph(figure=fig_total_pnl),

    html.H3("📋 Summary Stats", style={"color": "white", "marginTop": "2rem"}),
    dash_table.DataTable(
        data=sentiment_df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in sentiment_df.columns],
        style_table={'overflowX': 'auto'},
        style_cell={'backgroundColor': '#1e1e1e', 'color': 'white', 'textAlign': 'center'},
        style_header={'backgroundColor': '#333', 'color': 'white', 'fontWeight': 'bold'}
    )
])

if __name__ == "__main__":
    app.run(debug=True)
