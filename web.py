import streamlit as st
st.write("Choose your recipe:")
if st.button("Butter Chicken"):
    st.switch_page("pages/butter_chicken.py")
if st.button("Pizza"):
    st.switch_page("pages/pizza.py")
if st.button("Chocolate Cake"):
    st.switch_page("pages/chocolate_cake.py")