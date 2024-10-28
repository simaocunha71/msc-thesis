def text_lowercase_underscore(s):
    return bool(re.findall(r'[a-z]+_[a-z]+', s))