    return ''.join(c.lower() if c.isupper() else c.upper() for c in s[::-1]) if any(c.isalpha() for c in s) else s[::-1]


