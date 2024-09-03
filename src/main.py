from openai import OpenAI
import os
from dotenv import load_dotenv

from utils.yaml_utils import load_yaml_file
from utils.api_utils import generate_cover_letter
from utils.format_utils import format_cover_letter
from utils.html_utils import write_to_html
from utils.pdf_utils import create_pdf
from utils.prompt_utils import create_prompt

load_dotenv()
key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=key)

applicant_data=load_yaml_file('resume.yaml')

job_description=input("Enter the Job Description:\n")

prompt=create_prompt(applicant_data=applicant_data, job_description=job_description)

cover_letter=generate_cover_letter(client=client, prompt=prompt)

formatted_cover_letter=format_cover_letter(cover_letter_text=cover_letter, template_path='templates', template_file='cover_letter_template.html')

write_to_html(content=formatted_cover_letter, html_file='res/cover_letter.html')

create_pdf(cover_letter=cover_letter, output_path='res/cover_letter.pdf')

