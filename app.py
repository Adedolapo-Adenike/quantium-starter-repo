import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load and sort the data
df = pd.read_csv('formatted_sales_data.csv')
df = df.sort_values('date')

# Build the line chart
fig = px.line(
    df,
    x='date',
    y='sales',
    title='Pink Morsel Sales Over Time',
    labels={'date': 'Date', 'sales': 'Sales ($)'}
)

# Build the Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1('Pink Morsel Sales Visualiser'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)