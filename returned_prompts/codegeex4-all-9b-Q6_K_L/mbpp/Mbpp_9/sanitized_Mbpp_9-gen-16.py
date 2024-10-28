def find_Rotations(string):
    size = len(string)
    for i in range(1, size):
        if string[i:] + string[:i] == string:
            return i
    return -1