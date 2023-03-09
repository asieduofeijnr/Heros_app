import streamlit as st
import time
import requests
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


#hide the sidebar including all items in it
st.set_page_config(initial_sidebar_state="collapsed")
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)

#import lottie animations from lottie website
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_ykgoqtuj.json")

st_lottie(lottie_hello, key="hello_animation")
st.title("Welcome to Heros")

#Take parents details
st.text_input(" ",placeholder="Parents Name", key= "Parent")
st.text_input(" ",placeholder="Wards Name", key= "Child")
st.text_input(" ",placeholder="E-mail", key= "Mail")
st.text_input(" ",placeholder="Password", key= "Password")
st.text_input(" ",placeholder="Phone Number", key= "Phone_number")

add_vertical_space(2)


if st.button("REGISTER"):
    switch_page("welcome_page")


st.session_state