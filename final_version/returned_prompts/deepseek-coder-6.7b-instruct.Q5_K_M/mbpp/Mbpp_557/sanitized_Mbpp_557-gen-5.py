def toggle_string(s):
    result = ''
    for char in s:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result