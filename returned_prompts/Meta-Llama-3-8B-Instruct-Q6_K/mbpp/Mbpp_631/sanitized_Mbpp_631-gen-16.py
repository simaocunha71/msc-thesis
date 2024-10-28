def replace_spaces(s):
    result = ""
    for char in s:
        if char == " ":
            result += "_"
        elif char == "_":
            result += " "
        else:
            result += char
    return result