def toggle_string(s):
    lower = [chr(ord(c) - 32) if c.isupper() else chr(ord(c) + 32) for c in s]
    upper = [chr(ord(c) - 32) if c.islower() else chr(ord(c) + 32) for c in s]
    return ''.join(lower), ''.join(upper)