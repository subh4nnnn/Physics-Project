import requests
import pandas as pd

#Fetch the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_physical_quantities"
my_headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=my_headers)

#read_html looks for tables
tables = pd.read_html(response.text)

#select the respectful tables
scalar_df = tables[0]
vector_df = tables[2]
tensor_df = tables[4]

#choose the columns i need and drop the rest
col = ["Name", "Symbol", "Description", "SI unit", "Quantity dimension"]
scalar_df = scalar_df[col]
vector_df = vector_df[col]
tensor_df = tensor_df[col]

#add column 'Type'
scalar_df["Type"] = "Scalar"
vector_df["Type"] = "Vector"
tensor_df["Type"] = "Tensor"

#concatinate all the dataframes into one
df = pd.concat([scalar_df, vector_df, tensor_df], ignore_index=True)

#this creates a .json file thats readable
df.to_json("physics_quantities.json", orient="records", indent=4)
