def replace_spaces(string: str):
    if ' ' in string:
        return string.replace(' ', '_')
    else:
        return string.replace('_', ' ')