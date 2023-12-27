import streamlit as st
import pandas as pd
import plotly.express as px

sidebar = st.sidebar.radio('Choose:',['Data', 'Insights', 'Prediction'])
data = pd.read_csv('dataset.csv')

data = data[:1000]

st.title('Dataset Information')

st.header('Data Frame Information')
st.dataframe(data=data)


payment_type = data['type']
fig = px.histogram(payment_type, title='Payment Type Distribution', x='type')

st.header('Payment Types')
st.plotly_chart(fig, theme="streamlit", use_container_width=True)



# Sample data (replace this with your actual data)
dataset_fraud = data['isFlaggedFraud']

print(list(data['isFlaggedFraud']).count('1'))
# dataset_fraud = {'Category': ['Fraud', 'Verified'],
#         'Values': [data['isFlaggedFraud'].value_counts().get('1', 0), data['isFlaggedFraud'].value_counts().get('0', 0)]}
# df = pd.DataFrame(data)

# # Create a horizontal bar chart using plotly.express
# fig = px.bar(df, x='Values', y='Category', orientation='h', title='Horizontal Bar Chart')

# # Display the chart in Streamlit
# st.plotly_chart(fig)










