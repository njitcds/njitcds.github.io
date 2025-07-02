import streamlit as st
import pandas as pd
import io

st.set_page_config("Application Per Job", "🗒️")

# Function to remove duplicates and calculate application number
def process_sheet1(df):
    with st.spinner("Finding Application Number per Job..."):
        # Copy columns to new DataFrame (Sheet2)
        sheet2 = df[['Employer Name', 'Job Title', 'Job ID']].copy().fillna("Not Found")
        # Remove duplicates based on 'Employer Name' and 'Job Title'
        sheet2 = sheet2.drop_duplicates(subset=['Employer Name', 'Job Title'], keep="first")
        # Calculate the application number
        df['Application Number'] = df.groupby(['Employer Name', 'Job Title'])['Job ID'].transform('count')
        sheet2 = sheet2.merge(df[['Employer Name', 'Job Title', 'Application Number']].drop_duplicates(), 
                              on=['Employer Name', 'Job Title'], 
                              how='left')
    
    st.success("Duplicates are Removed & Application number is counted.")
    return sheet2

# Function to perform XLOOKUP-like operation and add multiple return columns
def perform_xlookup(sheet2, sheet3):
    with st.spinner("Looking up Job Specific Details..."):
        return_cols = [
            'Job Type Name', 'Postings Created At Date', 'Postings Expiration Date Date', 
            'Locations State', 'Job Contacts First Name', 'Job Contacts Last Name', 
            'Job Contacts Email Address', 'Job Contacts Phone', 'Employer Name', 'Employer Employer State'
        ]
        
        lookup_col = 'Jobs ID'

        # Ensure the lookup column in sheet3 is unique
        sheet3 = sheet3.drop_duplicates(subset=[lookup_col], keep="first").fillna("Not Found")

        for col in return_cols:
            sheet2[col] = sheet2['Job ID'].map(sheet3.set_index(lookup_col)[col]).fillna("Not Found")
    
    st.success("Process Completed!")
    return sheet2

def more_than_ten(sheet2):
    sheet4 = sheet2[sheet2['Application Number'] > 10].fillna("Not Found")
    return sheet4

def more_than_ten_unique(sheet4):
    sheet5 = sheet4.copy().fillna("Not Found")
    # Remove duplicates based on 'Employer Name'
    sheet5 = sheet5.drop_duplicates(subset=['Employer Name'], keep="first")
    return sheet5

def convert_csv_to_excel(file):
    try:
        df = pd.read_csv(file, encoding='utf-8', on_bad_lines='warn')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(file, encoding='ISO-8859-1', on_bad_lines='warn')
        except UnicodeDecodeError:
            df = pd.read_csv(file, encoding='utf-16', on_bad_lines='warn')
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    return output.getvalue()

def ensure_arrow_compatibility(df):
    # Convert datetime columns to string
    for col in df.select_dtypes(include=['datetime', 'datetimetz']).columns:
        df[col] = df[col].astype(str)
    
    # Convert object columns with mixed types to string
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str)
    
    return df

def main():
    st.title("Application Per Job")

    if 'sheet2' not in st.session_state:
        st.session_state['sheet2'] = None

    # Upload the first file (CSV or Excel)
    file1 = st.file_uploader("Upload First (Part 1 Report) File (CSV or Excel)", type=["csv", "xlsx"])
    if file1 is not None:
        if file1.name.endswith('.csv'):
            file1_excel = convert_csv_to_excel(file1)
            df1 = pd.read_excel(io.BytesIO(file1_excel), sheet_name=0).fillna("Not Found")
        else:
            df1 = pd.read_excel(file1, sheet_name=0).fillna("Not Found")
        
        st.write("First File - Sheet 1:")
        df1 = ensure_arrow_compatibility(df1)
        st.dataframe(df1)

        # Process the first file to create sheet2
        st.session_state['sheet2'] = process_sheet1(df1)
        st.write("Processed Data - Sheet 2:")
        st.write(st.session_state['sheet2'])

        # Upload the second file (CSV or Excel)
        file2 = st.file_uploader("Upload Second (Part 2 Report) File (CSV or Excel)", type=["csv", "xlsx"])
        if file2 is not None:
            if file2.name.endswith('.csv'):
                file2_excel = convert_csv_to_excel(file2)
                df2 = pd.read_excel(io.BytesIO(file2_excel), sheet_name=0).fillna("Not Found")
            else:
                df2 = pd.read_excel(file2, sheet_name=0).fillna("Not Found")
            
            st.write("Data from Second File - Sheet 3:")
            df2 = ensure_arrow_compatibility(df2)
            st.dataframe(df2)

            # Add the second file data to sheet3
            sheet3 = df2.copy()

    if 'sheet2' in st.session_state and st.session_state['sheet2'] is not None and file2 is not None:
        # Perform XLOOKUP-like operation
        final_sheet2 = perform_xlookup(st.session_state['sheet2'], sheet3)
        st.write("Final Processed Data with XLOOKUP Result:")
        final_sheet2 = ensure_arrow_compatibility(final_sheet2)
        st.write(final_sheet2)
        sheet4 = more_than_ten(final_sheet2)
        sheet5 = more_than_ten_unique(sheet4)

        # Option to download the final processed file
        with pd.ExcelWriter("application_per_job.xlsx") as writer:
            final_sheet2.to_excel(writer, sheet_name='Final Report', index=False)
            sheet4.to_excel(writer, sheet_name='More Than 10 Applications', index=False)
            sheet5.to_excel(writer, sheet_name='Unique Employers', index=False)
        
        with open("application_per_job.xlsx", "rb") as file:
            st.info("Now You can Download the File by Clicking on Download Button.")
            btn = st.download_button(
                label="Download Processed File",
                data=file,
                file_name="application_per_job.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

if __name__ == "__main__":
    main()