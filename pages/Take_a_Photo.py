import streamlit as st
import time
import datetime
import functions
from main import *


from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

#Page setting and hidinng the sidebar including all items in it
st.set_page_config(page_title="Little Heros", page_icon=":baby:",layout="centered", initial_sidebar_state="collapsed")
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)


#put lottie jsonn file into variable to be loaded into streamlit    
w_iconlottie = functions.load_lottiefile("lottie_files/w_icon.json")

#parameter for lottie w_icon animation file

# st_lottie(w_iconlottie, 
#           key="w_icon",
#           height= 256,
#           width = 256)


if st.button("<<Back"):
    switch_page("main")

st.title("You are registerd. Please take a Photo.")


parent_picture = st.camera_input(label=" ", key="Parent_picture")

if parent_picture:
    if st.button("Great Selfie - Click this button to proceed to class or click clear photo above to take again"):
        message = f'''\
Subject:Sign in from {the_email}

Parents Name: {the_parent_firstname} {the_parent_lastname}
Ward Name: {the_child_firstname} {the_child_lastname}
Parents Contact: {the_phone_number}
'''
        functions.send_email(message)
        switch_page("Welcome_to_class")




    st.session_state

