import streamlit as st 
import yfinance as yf
import pandas as pd
from util.company import companyName
# from util.dateCheck import checkDat


# st.beta_set_page_config(page_title='Stock Market History ',page_icon=":smiley:")

# Title and Heading 

st.title(""" 

   Stock Market History 

""")

# Company 

company_choice =  st.sidebar.selectbox("Company Selection", ("GOOGLE", "APPLE", "MICROSOFT"))
st.sidebar.header("Date Range")
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')
submit = st.sidebar.button('View Chart')

# Check the Choice 
st.write("Company Chosen : ",company_choice)
st.write("Start Date : ",start_date)
st.write("End Date : ",end_date)

# get the data of campany 
company_data = yf.Ticker(companyName(company_choice))

# Get Historical Data of the Company 
trackDate = company_data.history(period='1d', start = start_date, end=end_date)

if submit:
   # Draw the Graph
   st.write("## Closing Price ")
   st.line_chart(trackDate.Close)
   st.write("## Volume Price ")
   st.line_chart(trackDate.Volume)
