def toggle_string(s):
    return ''.join(chr(256 - ord(c)) if c.isalpha() else c for c in s)