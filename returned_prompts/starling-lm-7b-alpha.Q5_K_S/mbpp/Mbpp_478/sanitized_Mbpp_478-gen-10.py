def remove_lowercase(s):
    return s.replace(str(c) for c in s if c.islower() )