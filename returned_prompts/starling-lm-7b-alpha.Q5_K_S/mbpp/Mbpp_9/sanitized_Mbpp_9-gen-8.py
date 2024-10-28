def find_Rotations(string):
    length = len(string)
    for i in range(1,length):
        if string[:i] == string[-i:]:
            return i
    return length