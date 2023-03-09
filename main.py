import streamlit as st
import time
import functions


from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


#hide the sidebar including all items in it
st.set_page_config(initial_sidebar_state="collapsed")
st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)


#put lottie jsonn file into variable to be loaded into streamlit    
w_iconlottie = functions.load_lottiefile("lottie_files/w_icon.json")

#parameter for lottie w_icon animation file
st_lottie(w_iconlottie, 
          key="w_icon",
          height= 256,
          width = 256)



#Header
st.title("Welcome to Little Heros :wave:")


with st.container():
#Take parents details
    st.text_input(" ",placeholder="Parents First Name", key= "Parent_firstname")
    st.text_input(" ",placeholder="Parents Last Name", key= "Parent_lastname")
    st.text_input(" ",placeholder="Wards First Name", key= "Child_firstname")
    st.text_input(" ",placeholder="Wards Last Name", key= "Child_lastname")
    st.text_input(" ",placeholder="E-mail", key= "Mail")
    st.text_input(" ",placeholder="Password", key= "Password")
    st.text_input(" ",placeholder="Phone Number", key= "Phone_number")

add_vertical_space(2)


the_parent_firstname = st.session_state["Parent_firstname"]
the_parent_lastname = st.session_state["Parent_lastname"]
the_child_firstname = st.session_state["Child_firstname"]
the_child_lastname = st.session_state["Child_lastname"]
the_email = st.session_state["Mail"]
the_password = st.session_state["Password"]
the_phone_number = st.session_state["Phone_number"]


if st.button("Take a Photo"):
    #Validation for email
    if the_parent_firstname == "":
        st.error("Please insert your last name")
    if the_parent_lastname == "":
        st.error("Please insert your last name")
    if the_child_firstname == "":
        st.error("Please insert your wards first name")
    if the_child_lastname == "":
        st.error("Please insert your wards last name")
    if not functions.check(the_email) or the_email == "":
        st.error("Invalid email: Please type a correct email like hello@littleheros.com")
    if the_password == "":
        st.error("Please insert a password:")
    if functions.validate_password(the_phone_number) or the_phone_number == "":
        st.error("Please insert a Valid Phone Number:")       
    else:
        switch_page("Take a photo")


st.session_state