def find_Rotations(s):
    n = len(s)
    for i in range(1, n):
        if s[i:] + s[:i] == s:
            return i
    return 0