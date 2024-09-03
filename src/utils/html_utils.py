def write_to_html(content, html_file="res/cover_letter.html", ):
    with open(html_file, mode='w') as file:
        file.write(content)