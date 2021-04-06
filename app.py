import streamlit as st 



# Title and Heading 

st.title(""" 

   Stock Market History 

""")

# Company 

company_choice =  st.sidebar.selectbox("Company Selection", ("APPLE", "GOOGLE", "FACEBOOK"))
