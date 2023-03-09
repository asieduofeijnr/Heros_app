import streamlit as st

#hide the sidebar including all items in it
st.set_page_config(initial_sidebar_state="collapsed")
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)

st.title("You are registerd. Please take your child in.")