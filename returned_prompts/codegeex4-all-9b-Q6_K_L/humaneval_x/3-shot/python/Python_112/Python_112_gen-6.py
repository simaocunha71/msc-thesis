    new_string = ""
    for c in s:
        if c not in c:
            new_string += c
    if new_string == new_string[::-1]:
        return (new_string, True)
    else:
        return (new_string, False)

