def remove_lowercase(string):
    for ch in string:
        if ch.islower():
            string = string.replace(ch, '')
    return string