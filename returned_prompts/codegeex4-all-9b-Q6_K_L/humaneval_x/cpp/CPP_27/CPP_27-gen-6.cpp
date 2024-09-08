def flip_case(string):
    string2 = ""
    for i in range(len(string)):
        if string[i].islower():
            string2 += string[i].upper()
        elif string[i].isupper():
            string2 += string[i].lower()
    return string2

