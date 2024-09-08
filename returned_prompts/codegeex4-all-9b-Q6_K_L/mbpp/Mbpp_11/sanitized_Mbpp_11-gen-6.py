def remove_Occ(string, char):
    if string[0] == char:
        string = string[1:]
    if string[-1] == char:
        string = string[:-1]
    return string