import streamlit as st
import pandas as pd
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

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

def get_worksheet():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=scopes
    )
    client = gspread.authorize(creds)
    sheet = client.open("physics_quantity_suggestions")
    return sheet.sheet1

st.markdown("---")
st.subheader("Suggest a missing quantity")
with st.form("missing_quantity_form"):
    user_name = st.text_input("Your name: *")
    quantity_name = st.text_input("Quantity name: *")
    submitted = st.form_submit_button("Submit suggestion")

if submitted:
    if quantity_name.strip() == "" or user_name.strip() == "":
        st.error("Please enter both your name and the quantity name")
    else:
        ws = get_worksheet()
        ws.append_row([
            user_name.strip(),
            quantity_name.strip(),
            datetime.now().isoformat()
        ])
        st.success("Your suggestion has been submitted")


st.markdown("---")
st.caption("Reference / Notes")
st.caption("https://en.wikipedia.org/wiki/List_of_physical_quantities")
