def text_lowercase_underscore(s):
    if not s:
        return False
    result = True
    temp = ''
    for char in s:
        if char.islower():
            temp += char
        elif temp:
            if '_' not in temp:
                result = False
                break
            temp = ''
        else:
            result = False
            break
    if temp and '_' not in temp:
        result = False
    return result