def remove_lowercase(s):
    result = ""
    for i in s:
        if i.isupper():
            result += i
    return result