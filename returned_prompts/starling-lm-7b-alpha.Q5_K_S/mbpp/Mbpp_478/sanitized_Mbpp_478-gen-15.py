def remove_lowercase(s):
    new_str = ""
    for i in s:
        if i.isupper():
            new_str += i
    return new_str