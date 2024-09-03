from jinja2 import Environment, FileSystemLoader

def format_cover_letter(cover_letter_text, template_path='templates', template_file='cover_letter_template.html'):
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template(template_file)
    rendered_letter = template.render(cover_letter=cover_letter_text.replace('\n', '<br>').replace('\n\n', '</p><p>').replace('**',''))
    return rendered_letter

