def replace_specialchar(text):
    for specialchar in [',', '.', ' ']:
        text = text.replace(specialchar, ':')
    return text



