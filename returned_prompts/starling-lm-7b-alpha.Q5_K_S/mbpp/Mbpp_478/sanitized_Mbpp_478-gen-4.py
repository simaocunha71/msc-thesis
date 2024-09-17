def remove_lowercase(string):
    new_str = ""
    for i in range(len(string)):
        if string[i].isupper():
            new_str += string[i]
    return new_str