import streamlit as st
import pandas as pd

st.title("Physics Quantities Finder")
st.write("Search for a physics quantity and get its details")

phy_df = pd.read_json("physics_quantities.json")
query = st.text_input("Enter quantity name:")

if query:
    mask = phy_df["Name"].str.lower() == query.lower()
    result = phy_df[mask]

    if not result.empty:
        first_row = result.iloc[0]
        st.write("**Name:**", first_row["Name"])
        st.write("**Symbol:**", first_row["Symbol"])
        st.write("**Description:**", first_row["Description"])
        st.write("**SI unit:**", first_row["SI unit"])
        st.write("**Quantity dimension:**", first_row["Quantity dimension"])
        st.write("**Type:**", first_row["Type"])
    else:
        st.warning("Quantity not found on Wikipedia")

st.markdown("---")
st.caption("Reference / Notes")
st.caption("https://en.wikipedia.org/wiki/List_of_physical_quantities")
