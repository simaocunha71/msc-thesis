def replace_specialchar(text):
    for i in [' ', ',', '.']:
        text = text.replace(i, ':')
    return text