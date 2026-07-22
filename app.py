import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load and sort the data
df = pd.read_csv('formatted_sales_data.csv')
df = df.sort_values('date')

# Build the Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        'Pink Morsel Sales Visualiser',
        id='header',
        style={
            'textAlign': 'center',
            'color': '#4a2c2a',
            'fontFamily': 'Arial, sans-serif',
            'marginTop': '30px'
        }
    ),
    html.Div([
        dcc.RadioItems(
            id='region-picker',
            options=['north', 'east', 'south', 'west', 'all'],
            value='all',
            inline=True,
            labelStyle={'marginRight': '20px', 'fontSize': '18px'},
            style={'textAlign': 'center', 'marginBottom': '20px'}
        )
    ]),
    html.Div([
        dcc.Graph(id='visualization')
    ], style={'width': '80%', 'margin': '0 auto'})
], style={
    'backgroundColor': '#fdf0f0',
    'fontFamily': 'Arial, sans-serif',
    'paddingBottom': '40px'
})

@app.callback(
    Output('visualization', 'figure'),
    Input('region-picker', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        title='Pink Morsel Sales Over Time',
        labels={'date': 'Date', 'sales': 'Sales ($)'}
    )
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        title_font_size=20
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)