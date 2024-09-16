def text_lowercase_underscore(text):
    pattern = r"[a-z]+_[a-z]+"
    return re.search(pattern, text) is not None


