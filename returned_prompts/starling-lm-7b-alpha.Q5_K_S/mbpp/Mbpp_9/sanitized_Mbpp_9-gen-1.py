def find_Rotations(string):
    # Get length of string
    length = len(string)
    for i in range(length):
        if string[:i] == string[-i:]:
            return i