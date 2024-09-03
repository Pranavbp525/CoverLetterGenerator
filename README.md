# Cover Letter Generator

This project is a Streamlit web application that generates customized cover letters based on a provided job description and applicant data. The generated cover letters can be viewed in the app, regenerated if needed, and downloaded as a PDF.

## Features

- **Input Job Description:** Users can input a job description in the text area.
- **Generate Cover Letter:** The app uses OpenAI's GPT model to generate a tailored cover letter based on the provided job description and applicant data from a YAML file.
- **Regenerate Cover Letter:** Users can regenerate the cover letter with the same job description.
- **Download as PDF:** Users can download the generated cover letter as a PDF.

## Requirements

- Python 3.10+
- Streamlit
- OpenAI API Key
- `fpdf` for PDF generation
- `jinja2` for HTML templating

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Pranavbp525/CoverLetterGenerator.git
   cd CoverLetterGenerator
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. **Prepare the YAML file:**

   Ensure you have a `resume.yaml` file in the root directory containing the applicant's information.

2. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

3. **Interact with the app:**

   - Enter the job description in the text area.
   - Click on the "Generate Cover Letter" button to generate the cover letter.
   - View the cover letter directly in the app.
   - Click "Download PDF" to download the generated cover letter.
   - Click "Regenerate" to generate a new cover letter with the same job description.

## File Structure

- `app.py`: Main entry point of the Streamlit app.
- `src/`: Contains utility functions for loading YAML, generating cover letters, formatting, and saving files.
  - `yaml_utils.py`
  - `api_utils.py`
  - `format_utils.py`
  - `html_utils.py`
  - `pdf_utils.py`
  - `prompt_utils.py`
- `templates/`: Contains HTML templates for formatting the cover letter.
- `res/`: Directory where the generated HTML and PDF files are stored.
- `requirements.txt`: List of Python dependencies.
- `.env`: Environment variables file (not included in the repository for security reasons).

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
