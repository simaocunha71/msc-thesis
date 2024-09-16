def toggle_string(s):
    if not s:
        return s
    if s[0].islower():
        return s.title()
    else:
        return s.lower()