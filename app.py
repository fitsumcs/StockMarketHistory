import streamlit as st 
import yfinance as yf
import pandas as pd



# Title and Heading 

st.title(""" 

   Stock Market History 

""")

# Company 

company_choice =  st.sidebar.selectbox("Company Selection", ("goog", "aapl", "msft","SPY", "AAPL"))
st.sidebar.header("Date Range")
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')
submit = st.sidebar.button('View Chart')

# Check the Choice 
st.write(company_choice)
st.write(start_date)
st.write(end_date)

# get the data of campany 
company_data = yf.Ticker(company_choice)

# Get Historical Data of the Company 
trackDate = company_data.history(period='1d', start = start_date, end=end_date)

if submit:
    # Draw the Graph
    st.line_chart(trackDate.Close)
    st.line_chart(trackDate.Volume)