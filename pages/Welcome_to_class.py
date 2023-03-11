import streamlit as st
import time
import functions


from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

#Page setting and hidinng the sidebar including all items in it
st.set_page_config(page_title="Little Heros", page_icon=":baby:",layout="centered", initial_sidebar_state="collapsed")
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)


#put lottie jsonn file into variable to be loaded into streamlit    
w_icon = functions.load_lottiefile("lottie_files/w_icon.json")
hero_icon = functions.load_lottiefile("lottie_files/hero_icon.json")

#parameter for lottie w_icon animation file
# st_lottie(w_icon, 
#           key="w_icon",
#           height= 256,
#           width = 256)

st.title("Please take your little hero to class.")

#parameter for lottie w_icon animation file
st_lottie(hero_icon, 
          key="hero_icon",
          height= 256,
          width = 256)

if functions.countdown(0,0,5):
    switch_page("main")

st.session_state

