def toggle_string(s):
    result = ""
    for char in s:
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
    return result