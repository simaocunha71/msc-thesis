def remove_uppercase(s):
    result = ""
    for char in s:
        if char.islower():
            result += char
    return result

