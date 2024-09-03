from datetime import datetime

def create_prompt(applicant_data, job_description):
    personal_info = f"""
**Applicant's Personal Information:**
Name: {applicant_data['personal_information']['name']} {applicant_data['personal_information']['surname']}
Email: {applicant_data['personal_information']['email']}
Phone Number: {applicant_data['personal_information']['phone_prefix']} {applicant_data['personal_information']['phone']}
"""

    education_details = f"""
**Applicant's Education Details:**
Education: {', '.join([edu['degree'] + ' in ' + edu['field_of_study'] + ' from ' + edu['university'] + ' with ' + edu['gpa'] + ' GPA' for edu in applicant_data['education_details']])}
Course Work: {', '.join([', '.join(edu['courses']) for edu in applicant_data['education_details']])}
"""

    experience_details = "\n".join([
        f"Worked as {exp['position']} at {exp['company']} where the job responsibilities include:\n  - " +
        '\n  - '.join(exp['key_responsibilities']) +
        f"\n  - Skills Acquired: {', '.join(exp['skills_acquired'])}\n"
        for exp in applicant_data['experience_details']
    ])

    projects_details = "\n".join([
        f"Created a project titled {proj['name']}. Description of the Project:\n  - " +
        '\n  - '.join(proj['description']) + "\n"
        for proj in applicant_data['projects']
    ])

    skills_details = f"""
**Applicant's Skills:**
Certifications: {', '.join(applicant_data['certifications'])}
Programming Languages: {', '.join(applicant_data['skills']['programing_languages'])}
Databases: {', '.join(applicant_data['skills']['databases'])}
Frameworks: {', '.join(applicant_data['skills']['frameworks'])}
Tools: {', '.join(applicant_data['skills']['tools'])}
Cloud: {', '.join(applicant_data['skills']['cloud'])}
"""

    job_description_section = f"""
**Job Description:**
{job_description}
"""

    cover_letter_requirements = """
**Cover Letter Requirements:**
- Address the letter to the appropriate hiring manager or use a generic salutation if not specified.
- Do not include a section for the company's address, city, state or zip code.
- Introduce the applicant and express enthusiasm for the position.
- Highlight relevant education, experience, skills, and projects that match the job requirements.
- Explain why the applicant is a good fit for the role and the company.
- Conclude with a polite call to action and sign off appropriately.
- Maintain a professional and formal tone throughout.
- The letter should be around 400-500 words.
- It is very important to the applicant's career that the cover letter contents are the most relevant to the job description in the applicants information provided.

Please write the cover letter below:
"""

    prompt = f"""
Using the applicant's information and the job description provided, write a personalized and professional cover letter.

---
Today's date is: {datetime.now().date()}
{personal_info}
{education_details}
**Applicant's Work Experience Details:**
{experience_details}
**Applicant's Personal Projects:**
{projects_details}
{skills_details}

---

{job_description_section}

---

{cover_letter_requirements}
"""

    return prompt