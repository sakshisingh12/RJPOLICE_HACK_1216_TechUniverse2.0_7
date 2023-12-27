# app.py
from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

# Load your dataset
data = pd.read_csv('dataset.csv')
# data = data[:50000]

@app.route('/')
def index():
    # Basic dataset information
    head_info = data.head().to_html(classes='table table-striped table-bordered')

    # Basic statistics
    stats_info = data.describe().to_html(classes='table table-striped table-bordered')

    # Bar chart using Plotly Express
    histogram = px.histogram(data, x='type', title='Histogram for Payment Types')

    # Save the bar chart as HTML
    histogram_html = histogram.to_html(full_html=False)
    
    flagged_fraud = px.histogram(data, x='isFlaggedFraud')
    flagged_fraud_html = flagged_fraud.to_html(full_html=False)

    return render_template("index.html", head_info=head_info, 
        stats_info=stats_info, bar_chart_html=histogram_html,
        flagged_fraud_html=flagged_fraud_html)

if __name__ == '__main__':
    app.run(debug=True)
