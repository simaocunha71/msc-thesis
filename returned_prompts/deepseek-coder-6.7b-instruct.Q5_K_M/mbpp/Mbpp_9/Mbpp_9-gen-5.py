
def find_Rotations(s):
    n = len(s)
    temp = s + s
    for i in range(1, n + 1):
        if temp[i:i + n] == s:
            return i
    return n


