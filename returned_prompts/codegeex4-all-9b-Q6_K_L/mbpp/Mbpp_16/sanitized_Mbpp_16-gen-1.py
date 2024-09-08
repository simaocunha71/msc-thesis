def text_lowercase_underscore(text):
    import re
    pattern = r'^[a-z]+(_[a-z]+)*$'
    return bool(re.match(pattern, text))