def remove_uppercase(s):
    return ''.join(c for c in s if c.islower())  # or s.lower() if you want the whole string in lowercase