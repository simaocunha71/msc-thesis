def replace_spaces(string: str) -> str:
    return string.replace(' ', '_') if ' ' in string else string.replace('_', ' ')