def replace_specialchar(text):
    text = text.replace(' ', ':')
    text = text.replace(',', ':')
    text = text.replace('.', ':')
    return text