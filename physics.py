import streamlit as st
import pandas as pd
from datetime import datetime
import os

#helper function
def add_space(lines=1):
    for _ in range(lines):
        st.write("")

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

add_space(1)

#for quantity suggestions:
st.markdown("---")
st.subheader("Suggest a missing quantity")
with st.form("missing_quantity_form"):
    missing_name = st.text_input("Missing physical quantity name *")
    submitted = st.form_submit_button("Submit suggestion")

if submitted:
    if missing_name.strip() == "":
        st.error("Please enter a quantity name")
    else:
        data = {
            "quantity": [missing_name.strip()],
            "time": [datetime.now().isoformat()]
        }
        df_new = pd.DataFrame(data)
        file_path = "missing_quantities.csv"

        if os.path.exists(file_path):
            df_existing = pd.read_csv(file_path)
            df_all = pd.concat([df_existing, df_new], ignore_index=True)
        else:
            df_all = df_new

        df_all.to_csv(file_path, index=False)
        st.success("Your suggestion has been submitted")

st.markdown("---")
st.caption("Reference / Notes")
st.caption("https://en.wikipedia.org/wiki/List_of_physical_quantities")

