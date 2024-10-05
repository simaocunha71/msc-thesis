    return ''.join(c.upper() if c.islower() else c.lower() for c in s[::-1] if c.isalpha()) or s[::-1]


