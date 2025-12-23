import streamlit as st

quantities = {"velocity": "m/s",
              "mass": "kg",
              "time": "s"}

st.title("Physics Unit Finder")
st.write("Type a physics quantity")
user_input = st.text_input("Enter: ").lower().strip()

if user_input:
    if user_input in quantities:
        st.success(f"Unit: {quantities[user_input]}")
    else:
        st.error("Quantity not found")