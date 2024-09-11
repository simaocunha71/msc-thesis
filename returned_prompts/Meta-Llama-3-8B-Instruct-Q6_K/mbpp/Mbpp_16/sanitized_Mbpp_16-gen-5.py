def text_lowercase_underscore(s):
    pattern = r'[a-z]+_'
    return bool(re.findall(pattern, s))