def remove_lowercase(s):
    return ''.join([c for c in s if c.isupper()])
    # or return ''.join(filter(str.isupper, s))  # Python 3.7+
    # or return ''.join([c for c in s if c in s.upper()])  # Python 3.9+