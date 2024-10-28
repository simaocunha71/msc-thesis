
def find_Rotations(s):
    if len(s) == 0:
        return 0
    length = 0
    while s == s[length:]+s[:length]:
        length += 1
    return length


