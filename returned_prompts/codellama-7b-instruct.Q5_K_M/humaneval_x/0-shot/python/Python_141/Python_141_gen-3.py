
def file_name_check(file_name):
    if len(file_name) > 3 or file_name.count(".") != 1:
        return "No"
    elif file_name[0] not in ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z"]:
        return "No"
    elif file_name[-3:] not in ["txt", "exe", "dll"]:
        return "No"
    else:
        return "Yes"
    





