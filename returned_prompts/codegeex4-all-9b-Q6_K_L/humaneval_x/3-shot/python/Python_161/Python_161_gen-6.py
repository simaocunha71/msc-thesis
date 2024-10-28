    new_str = ""
    for i in s:
        if i.isalpha():
            if i.isupper():
                new_str += i.lower()
            else:
                new_str += i.upper()
        else:
            new_str += i
    return new_str[::-1]

