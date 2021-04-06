import streamlit as st 



# Title and Heading 

st.title(""" 

   Stock Market History 

""")

# Company 

company_choice =  st.sidebar.selectbox("Company Selection", ("APPLE", "GOOGLE", "FACEBOOK"))
st.sidebar.header("Date Range")
st.sidebar.date_input('start date')
st.sidebar.date_input('end date')
