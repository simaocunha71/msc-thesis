def remove_lowercase(s):
    return ''.join([c for c in s if c.isupper()])  # or return s.upper() if you want to keep the original case