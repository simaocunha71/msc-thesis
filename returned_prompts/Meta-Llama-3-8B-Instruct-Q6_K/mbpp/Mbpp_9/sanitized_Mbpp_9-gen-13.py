def find_Rotations(s):
    n = len(s)
    for i in range(1, n):
        if s == s[i:] + s[:i]:
            return i
    return n