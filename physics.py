import streamlit as st
import pandas as pd

st.title("Physics Quantities Finder")
st.write("Search for a physics quantity and get its details")

# Load the JSON file into a pandas DataFrame
# phy_df now holds all physics quantities and their details
phy_df = pd.read_json("physics_quantities.json")

query = st.text_input("Enter quantity name: ")

# Only run the following code if the user typed something
if query:
    # Create a mask (True/False for each row) where the Name column matches the query
    # .str.lower() makes the comparison case-insensitive
    mask = phy_df["Name"].str.lower() == query.lower()

    # Filter the DataFrame using the mask
    # result contains only rows that match the user's query
    result = phy_df[mask]

    # Check if the filtered result has at least one row
    if not result.empty:
        # Convert the DataFrame to a list of dictionaries (one dictionary per row)
        rows = result.to_dict(orient="records")  # Convert DataFrame to a list of dictionaries

        # Take the first dictionary from the list
        first_row = rows[0]  # Take the first dictionary

        # Display the dictionary as nicely formatted JSON in Streamlit
        st.json(first_row)  # Show it nicely in Streamlit
    else:
        # If no rows matched, show a warning message to the user
        st.warning("Quantity not found")
