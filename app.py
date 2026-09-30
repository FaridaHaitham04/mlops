import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

name = os.getenv("NAME")
student_id = os.getenv("ID")

st.title("CSV Reader")

st.write(f"Name: {name}")
st.write(f"ID: {student_id}")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("First 3 Rows")

    st.dataframe(df.head(3))