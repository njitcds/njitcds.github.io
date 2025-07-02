import streamlit as st

# Initialize session state variables
if 'show_html_generation' not in st.session_state:
    st.session_state.show_html_generation = False

if 'preview_clicked' not in st.session_state:
    st.session_state.preview_clicked = False

def reset_session_state():
    st.session_state.clear()
    st.experimental_rerun()

# Custom CSS to enhance the look of the app
st.markdown("""
    <style>
        .main-title {
            font-size: 2.5em;
            color: #CC0000;
            text-align: center;
            margin-bottom: 20px;
        }
        .header {
            color: #CC0000;
            font-size: 1.5em;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .subheader {
            color: #4CAF50;
            font-size: 1.2em;
            margin-top: 10px;
            margin-bottom: 10px;
        }
        .review-button, .preview-button, .generate-button, .refresh-button {
            background-color: #CC0000;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            display: inline-block;
            font-size: 16px;
            margin: 10px 2px;
            cursor: pointer;
            border-radius: 12px;
        }
        .refresh-button {
            background-color: #f44336;
        }
        .student-details {
            border: 1px solid #ddd;
            padding: 10px;
            margin-top: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the page
st.markdown('<div class="main-title">HTML Code Generator Tool for Intern & Co-op Contest</div>', unsafe_allow_html=True)

# Add refresh button to the sidebar
with st.sidebar:
    if st.button('Refresh', key='refresh', help="Click to reset all fields"):
        reset_session_state()



   

# General Questions Section
# This is the general question section of the app, 
# these question will be requrired once per year/entry regardless of how many students are there.
# it includes [year - Contest Year, video_url - URL for final video, news_link - link to njit news article (optional)]
st.markdown('<div class="header">Interns & Co-op - General Questions</div>', unsafe_allow_html=True)
year = st.number_input('What is the year for this interns and co-op survey:', min_value=2024, key='year')
video_url = st.text_input('Enter the final video url that you would like to use:', placeholder='https://www.canva.com/design/...')

news = st.radio('Is there News Article link that you want to include?', options=('Yes', 'No'), index=None)
news_link = st.text_input('Enter the link of the news article that you would like to include', placeholder='https://news.njit.edu/...') if news == 'Yes' else ''





# Student Specific Questions Section
# This is the student specific question of the app,
# these question needs to be answered 'x' amount of times for 'x' number of students.
# it includes [ ]
st.markdown('<div class="header">Interns & Co-op - Student Specific Questions</div>', unsafe_allow_html=True)
num_students = st.number_input('Enter the number of students:', min_value=1, max_value=10, value=1, step=1)

# Collect details for each student
students = []
for i in range(int(num_students)):
    with st.container():
        st.markdown(f'<div class="subheader">Student {i + 1} Details</div>', unsafe_allow_html=True)
        with st.expander("Expand to enter details", expanded=True):
            name = st.text_input(f'Name of Student {i + 1}:', placeholder='John Doe', key=f'name{i}')
            first_name, last_name = (name.split(maxsplit=1) + ['', ''])[:2]

            photo_link = st.text_input(f'Photo URL for Student {i + 1}:', key=f'photo{i}')
            if photo_link:
                try:
                    st.image(photo_link, caption='Preview of Uploaded Image')
                except Exception as e:
                    st.error(f"An error occurred while trying to display the image: {e}")

            photo_side = st.radio(f'Position in the photo for Student {i + 1}:',
                                  options=("Left", "Right", "Center"), index=None, key=f'photo_side{i}')
            photo_option = {'Left': 'left center', 'Right': 'right center', 'Center': 'top'}.get(photo_side, 'top')

            student_level = st.radio(f'Is Student {i + 1} Undergraduate or Graduate?', options=('Undergraduate', 'Graduate'), key=f'level{i}', index=None)
            major = st.text_input(f'Major of Student {i + 1}:', placeholder='B.S. Computer Science', key=f'major{i}')
            employer = st.text_input(f'Employer for Student {i + 1}:', placeholder='Amazon', key=f'employer{i}')
            job_type = st.radio(f'What is the role title {i + 1}?', options=('Intern', 'Co-op'), key=f'type{i}', index=None)
            job_title = st.text_input(f'Job Title for Student {i + 1}:', placeholder='Software Engineering Intern', key=f'title{i}')

            students.append({'name': name, 'first_name': first_name, 'last_name': last_name, 
                    'photo_link': photo_link, 'photo_option': photo_option, 
                    'student_level': student_level, 'major': major, 
                    'employer': employer, 'job_type': job_type, 'job_title': job_title})

# Optional: Display collected data for review
if st.button('Review Submitted Information', key='review', help="Click to review all the entered information"):
    for student in students:
        st.write(student)
    st.session_state.show_html_generation = True





# HTML Code Generator Section
# This is the html code generator and preview part, 
# it includes [the template code, code block to copy - final block, rendered html - to see how it looks]
if st.session_state.show_html_generation:
    st.markdown('<div class="header">Interns & Co-op - Generate HTML Code</div>', unsafe_allow_html=True)

    html_code = f"""
    <!-- {year} Winners Starts here -->
    <div style="margin-bottom: 60px;">
    <h4><strong>{year} Winners</strong></h4>
    <p style="margin-top: 0px;"><em><strong>View all {year} Intern & Co-op contestants: <a href="{video_url}">here</a>.</strong></em></p>
    """

    for student in students:
        html_code += f"""
        <div style="display: flex; align-items: stretch; margin-bottom: 20px;">
            <div style="flex-shrink: 0; width: 250px; height: 290px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
                <img alt="{student['name']}" class="media-element file-default" src="{student['photo_link']}" style="width: 100%; height: 100%; object-fit: cover; object-position: {student['photo_option']};" />
            </div>
            <div style="flex: 1 1 auto; display: flex; align-items: center; margin: 0 0 0 10px; width: 100%;">
                <p style="margin: 0; font-size: 0.961em;">
                    <strong>{student['student_level']} {student['job_type']}</strong><br />
                    {student['first_name']} {student['last_name']}<br />
                    <strong>Major:</strong> {student['major']}<br />
                    <strong>Employer:</strong> {student['employer']}<br />
                    <strong>Position:</strong> {student['job_title']}
                </p>
            </div>
        </div>
        """
    if news == 'Yes':
        html_code += f"""
        <strong style="margin-top: 0px;">Read about the students' experiences: <a href="{news_link}">here</a>.</strong>
        """
    html_code += "</div>"

    if st.button('See Preview', key='preview', help="Click to preview the generated HTML"):
        st.subheader('Rendered HTML')
        st.html(html_code)
        st.session_state.preview_clicked = True

    if st.session_state.preview_clicked:
        if st.button('Generate HTML', key='generate', help="Click to generate the HTML code"):
            st.subheader('Generated HTML Code')
            st.code(html_code, language='html')