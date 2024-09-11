def text_lowercase_underscore(s):
    return re.findall(r'[a-z]+_[a-z]+', s) != []
    # or return bool(re.findall(r'[a-z]+_[a-z]+', s))  # same result