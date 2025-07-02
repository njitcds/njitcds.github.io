# Application Per Job

## Overview
This Streamlit application allows users to upload two CSV or Excel files and processes the data to generate a final report. The app includes functionality to remove duplicates, calculate application numbers, and perform lookups to add additional details from a second file.

## Features
- Upload CSV or Excel files
- Remove duplicates based on specific columns
- Calculate application numbers per job
- Perform lookups to add additional job details
- Download the final processed report with renamed sheets

## How It Works
1. **Upload Files**: Users can upload two CSV or Excel files.
2. **Data Processing**: 
   - The first file is processed to remove duplicates and calculate application numbers.
   - The second file is used to perform lookups and add additional job details to the first file.
3. **Sheet Renaming**: The final processed report includes sheets with specific names: 'Application Details', 'Final Report', and 'Job Details'.
4. **Download Processed File**: The final processed report can be downloaded as an Excel file.

## Application Workflow
1. **Initialize Session State**: The app initializes the session state to track the uploaded files.
2. **Title and Sidebar Refresh Button**: The app sets the page title and includes a refresh button in the sidebar to reset the state.
3. **File Uploaders**: The app allows users to upload two CSV or Excel files.
4. **DataFrame Creation**: Based on the uploaded files, DataFrames are created, and leading/trailing whitespaces are stripped from column names.
5. **Remove Duplicates**: The app processes the first file to remove duplicates and calculate application numbers.
6. **Perform Lookups**: The app performs lookups to add additional job details from the second file to the first file.
7. **Sheet Renaming**: The final processed report includes sheets renamed to 'Application Details', 'Final Report', and 'Job Details'.
8. **Download Processed File**: The app includes a button to download the final processed report as an Excel file.

## Functions
### App.py
- **Process Sheet 1**:
    - `process_sheet1(df)`: Processes the first file to remove duplicates and calculate application numbers.
- **Perform XLOOKUP**:
    - `perform_xlookup(sheet2, sheet3)`: Performs lookups to add additional job details from the second file to the first file.
- **Convert CSV to Excel**:
    - `convert_csv_to_excel(file)`: Converts uploaded CSV files to Excel format.
- **Ensure Arrow Compatibility**:
    - `ensure_arrow_compatibility(df)`: Ensures the DataFrame is compatible with Arrow format by converting datetime columns to strings and handling mixed types.

## Installation
- This tool is designed using Python 3.11
1. Clone the repository:
    ```bash
    git clone https://github.com/njitcds/ApplicationPerJob.git
    cd ApplicationPerJob
    ```
2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3. Install all dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Activate the virtual environment:
    ```bash
    pipenv shell
    ```
5. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

## Usage
1. **Upload Files**:
   - Upload the first CSV or Excel file using the file uploader.
   - Upload the second CSV or Excel file using the file uploader.
2. **Download Processed File**:
   - Click the "Download Processed File" button to download the final processed report as an Excel file.

## Error Handling
- **Missing Columns**: Displays an error message if any required columns are missing from the uploaded files.
- **NaN Values**: Ensures all NaN values are replaced with empty strings to avoid issues.

## Dependencies
- `streamlit`
- `pandas`
- `openpyxl`
- `xlsxwriter`

## License
This project is licensed under the Custom NJIT CDS License.

## Development
This tool is intended to be used internally. If you wish to further develop or enhance it, here are some key points to consider:
- **Modularize Code**:
  - Break down the current monolithic script into smaller, reusable modules for better maintainability.
- **Error Handling and Logging**:
  - Implement more robust error handling and logging mechanisms to track issues and improve debugging.
  - Add specific error messages for different failure points in the data processing and download process.
- **User Authentication**:
  - Integrate user authentication to secure access to the application.
- **Configuration Management**:
  - Externalize configuration parameters to a config file or environment variables.
- **Data Validation**:
  - Add data validation checks before processing to ensure data integrity and consistency.

## Exe App Convertor Tool
- Refer to this readme page/repo to understand and learn how the Streamlit web app has been converted to an executable: [stlite desktop](https://github.com/whitphx/stlite/blob/main/packages/desktop/README.md).