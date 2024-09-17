def text_lowercase_underscore(text: str) -> bool:
    pattern = r"^[a-z]+(_[a-z]+)+$"
    if re.match(pattern, text):
        return True
    else:
        return False