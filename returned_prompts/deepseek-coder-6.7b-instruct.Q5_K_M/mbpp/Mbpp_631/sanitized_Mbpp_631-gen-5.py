def replace_spaces(s: str):
    return s.replace(' ', '_') if ' ' in s else s.replace('_', ' ')