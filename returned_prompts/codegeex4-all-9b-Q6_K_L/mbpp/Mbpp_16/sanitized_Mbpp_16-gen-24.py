def text_lowercase_underscore(text: str) -> bool:
    pattern = re.compile(r'^[a-z]+(_[a-z]+)*$')
    return bool(pattern.match(text))