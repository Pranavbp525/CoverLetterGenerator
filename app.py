import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
from src.utils.yaml_utils import load_yaml_file
from src.utils.api_utils import generate_cover_letter
from src.utils.format_utils import format_cover_letter
from src.utils.html_utils import write_to_html
from src.utils.pdf_utils import create_pdf
from src.utils.prompt_utils import create_prompt

# Load environment variables
load_dotenv()
key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=key)

# Streamlit app
st.title("Cover Letter Generator")

# Input fields
job_description = st.text_area("Enter the Job Description:")

# Initialize session state for cover letter
if 'cover_letter' not in st.session_state:
    st.session_state.cover_letter = None

if st.button("Generate Cover Letter"):
    if job_description:
        # Load applicant data
        applicant_data = load_yaml_file('resume.yaml')

        # Create prompt
        prompt = create_prompt(applicant_data=applicant_data, job_description=job_description)

        # Generate cover letter
        st.session_state.cover_letter = generate_cover_letter(client=client, prompt=prompt)

    else:
        st.error("Please enter the job description.")

# Display generated cover letter
if st.session_state.cover_letter:
    # Format and save HTML
    formatted_cover_letter = format_cover_letter(
        cover_letter_text=st.session_state.cover_letter,
        template_path='templates',
        template_file='cover_letter_template.html'
    )
    html_file = 'res/cover_letter.html'
    write_to_html(content=formatted_cover_letter, html_file=html_file)

    # Save PDF
    pdf_file = 'res/cover_letter.pdf'
    create_pdf(cover_letter=st.session_state.cover_letter, output_path=pdf_file)

    # Display HTML content
    st.markdown(st.session_state.cover_letter, unsafe_allow_html=True)

    # Download buttons
    st.download_button(
        label="Download PDF",
        data=open(pdf_file, 'rb').read(),
        file_name='cover_letter.pdf',
        mime='application/pdf'
    )

    if st.button("Regenerate"):
        # Regenerate cover letter
        applicant_data = load_yaml_file('resume.yaml')
        prompt = create_prompt(applicant_data=applicant_data, job_description=job_description)
        st.session_state.cover_letter = generate_cover_letter(client=client, prompt=prompt)
