from fpdf import FPDF

def create_pdf(cover_letter, output_path='res/cover_letter.pdf'):
    pdf = FPDF(format='letter')
    pdf.add_page()

    # Set font
    pdf.set_font("Arial", size=11)

    # Define margins
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    pdf.set_top_margin(20)
    pdf.set_auto_page_break(auto=True, margin=15)

    # Add a title or header
    pdf.set_font("Arial", 'B', size=11)

    replacements = {
        '\u2014': '-',  # Replace em dash with a simple hyphen
        '\u2013': '-',  # Replace en dash with a simple hyphen
        '\u2018': "'",  # Replace left single quote with a simple apostrophe
        '\u2019': "'",  # Replace right single quote with a simple apostrophe
        '\u201c': '"',  # Replace left double quote with a simple quotation mark
        '\u201d': '"',  # Replace right double quote with a simple quotation mark
        '**':''
    }
    

    # Add multi-line text
    pdf.set_font("Arial", size=11)
    text = cover_letter
    for old, new in replacements.items():
        text = text.replace(old, new)
    pdf.multi_cell(0, 5, text)  # Adjust line height as needed

    # Save the PDF
    pdf.output(output_path)