import pandas as pd
import streamlit as st
from io import BytesIO
import xlsxwriter
import numpy as np

# Function to split the DataFrame
def split_dataframe(df):
    split_index = len(df) // 2
    df1 = df.iloc[:split_index]
    df2 = df.iloc[split_index:]
    return df1, df2

# Function to convert DataFrame to Excel and return as a downloadable link
def to_excel(df1, df2):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df1.to_excel(writer, sheet_name='Part1', index=False)
    df2.to_excel(writer, sheet_name='Part2', index=False)
    writer.close()
    processed_data = output.getvalue()
    return processed_data

st.title("User Role Details Split")

uploaded_file = st.file_uploader("Upload TSV file", type="tsv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, sep='\t')

    # Display the actual size of the DataFrame
    st.write(f"Actual size of the DataFrame: {len(df)} rows")

    df1, df2 = split_dataframe(df)

    # Display the sizes of the split DataFrames
    st.write(f"Size of the first part: {len(df1)} rows")
    st.write(f"Size of the second part: {len(df2)} rows")

    if st.button('Generate Output'):
        # Convert the DataFrames to Excel format
        excel_data = to_excel(df1, df2)

        # Create download link for the Excel file
        st.download_button(label='Download Excel files',
                           data=excel_data,
                           file_name='split_data.xlsx',
                           mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

# To run the app, use the command: streamlit run app.py
