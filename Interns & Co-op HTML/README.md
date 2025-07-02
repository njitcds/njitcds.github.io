# HTML Code Generator Tool for Intern & Co-op Contest
This tool is designed to generate HTML code for Intern & Co-op contests. The tool allows users to input general contest details and specific details for multiple students, then generate and preview the resulting HTML code.

## Features
- **General Contest Details:** Collects information such as the year of the contest, a video URL, and an optional news article link.
- **Student Specific Details:** Collects detailed information for each student, including their name, photo URL, academic and professional details.
- **HTML Code Generation:** Generates HTML code based on the provided details and allows users to preview and generate the final code.
- **Refresh Button:** Allows users to reset all fields and start over.

## Getting Started
### Prerequisites
- Python 3.11
- Streamlit
- Pandas

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/intern-coop-html-generator.git
    ```
2. Navigate to the project directory:
    ```sh
    cd intern-coop-html-generator
    ```
3. Install the required packages:
    ```sh
    pip install streamlit pandas
    ```

### Usage
1. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```
2. Open your web browser and go to the provided URL (typically `http://localhost:8501`).
3. Fill out the general contest details and student-specific details as described below.

## Sections and Functionality
### General Contest Details
- **Year:** Enter the year for the interns and co-op survey.
- **Video URL:** Enter the final video URL to be used.
- **News Article Link (Optional):** Choose if there is a news article link to include. If 'Yes', provide the URL of the news article.
### Student Specific Details
- **Number of Students:** Specify the number of students to enter details for.
- **Student Details:** For each student, expand the section to enter their details:
  - **Name:** Enter the full name of the student.
  - **Photo URL:** Enter the URL of the student's photo.
  - **Photo Position:** Select the position of the student in the photo (Left, Right, Center).
  - **Academic Level:** Select if the student is an Undergraduate or Graduate.
  - **Major:** Enter the major of the student.
  - **Employer:** Enter the name of the student's employer.
  - **Role Title:** Select if the role is an Internship or Co-op.
  - **Job Title:** Enter the job title of the student.
### Review and Generate HTML
- **Review Submitted Information:** Click this button to review all entered information. This will display the information and allow you to proceed to the HTML generation section.
- **Generate HTML Code:** Once reviewed, the tool will generate HTML code based on the provided information.
  - **See Preview:** Click this button to see a rendered preview of the HTML.
  - **Generate HTML:** Click this button to generate and display the HTML code that can be copied and used.
### Refresh
- **Refresh Button:** Located in the sidebar, this button will reset all fields and restart the app.

## Custom CSS
Custom CSS is used to enhance the appearance of the app. This includes styling for titles, headers, subheaders, buttons, and student details containers.

## Example

Below is an example of the generated HTML code:

```html
<!-- 2024 Winners Starts here -->
<div style="margin-bottom: 60px;">
    <h4><strong>2024 Winners</strong></h4>
    <p style="margin-top: 0px;"><em><strong>View all 2024 Intern & Co-op contestants: <a href="https://www.canva.com/design/...">here</a>.</strong></em></p>

    <div style="display: flex; align-items: stretch; margin-bottom: 20px;">
        <div style="flex-shrink: 0; width: 250px; height: 290px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
            <img alt="John Doe" class="media-element file-default" src="https://example.com/photo.jpg" style="width: 100%; height: 100%; object-fit: cover; object-position: left center;" />
        </div>
        <div style="flex: 1 1 auto; display: flex; align-items: center; margin: 0 0 0 10px; width: 100%;">
            <p style="margin: 0; font-size: 0.961em;">
                <strong>Undergraduate Intern</strong><br />
                John Doe<br />
                <strong>Major:</strong> B.S. Computer Science<br />
                <strong>Employer:</strong> Amazon<br />
                <strong>Position:</strong> Software Engineering Intern
            </p>
        </div>
    </div>
    <strong style="margin-top: 0px;">Read about the students' experiences: <a href="https://news.njit.edu/...">here</a>.</strong>
</div>
```

Below is an skeleton template of the generated HTML code:

```html
<!-- 20xx Winners Starts here -->
<div style="margin-bottom: 60px;">
    <h4><strong>20xx Winners</strong></h4>
    <p style="margin-top: 0px;"><em><strong>View all 20xx Intern &amp; Co-op contestants: <a href="canva_link">here.</a></strong></em></p>

    <div style="display: flex; align-items: stretch; margin-bottom: 20px;">
        <div style="flex-shrink: 0; width: 250px; height: 290px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
            <img alt="Jeremy Bedient" class="media-element file-default" src="photo_link" style="width: 100%; height: 100%; object-fit: cover; object-position: left center;" />
        </div>
        <div style="flex: 1 1 auto; display: flex; align-items: center; margin: 0 0 0 10px; width: 100%;">
            <p style="margin: 0; font-size: 0.961em;">
                <strong>Undergraduate/Graduate Intern/Co-op</strong><br />
                First_Name (space) Last_Name<br />
                <strong>Major:</strong> Major_Name<br />
                <strong>Employer:</strong> Company_Name<br />
                <strong>Position:</strong> Job_Title
            </p>
        </div>
    </div> 
    <strong style="margin-top: 0px;">Read about First_Name'S experience:<a href="news_link"> here.</a></strong> 
</div>
```

## Development
1. **Understanding the Code**: Ensure you thoroughly understand the current structure and functionality of the app. The main sections are general questions, student-specific questions, review, and HTML generation.
2. **Adding New Features**: Follow the modular approach used in the current code. Create new functions or modules as needed and integrate them seamlessly into the existing structure.
3. **Testing**: Test new features thoroughly to ensure they do not break existing functionalities. Use Streamlit's built-in capabilities to display debug information if needed.
4. **Documentation**: Update the README and any other relevant documentation to reflect new features and changes.

## License
This project is licensed under the Custom NJIT CDS License.

## Exe App Convertor tool:
- Refer to this readme page/repo to understand and learn how the streamlit webapp has been converted to exe: <a href="https://github.com/whitphx/stlite/blob/main/packages/desktop/README.md">stlite desktop</a>