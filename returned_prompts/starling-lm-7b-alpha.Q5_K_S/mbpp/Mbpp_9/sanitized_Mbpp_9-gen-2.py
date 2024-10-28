def find_Rotations(s):
    l = len(s)
    for i in range(1, l):
        if s[:i] == s[i:] and s[:i] != s:
            return i
    return l