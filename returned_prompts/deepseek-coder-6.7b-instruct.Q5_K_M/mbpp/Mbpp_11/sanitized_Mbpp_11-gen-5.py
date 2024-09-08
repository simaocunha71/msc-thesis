def remove_Occ(string, char):
    string = list(string)
    for i in range(len(string)):
        if string[i] == char:
            string[i] = ""
            break
    for i in range(len(string)-1, -1, -1):
        if string[i] == char:
            string[i] = ""
            break
    return "".join(string)