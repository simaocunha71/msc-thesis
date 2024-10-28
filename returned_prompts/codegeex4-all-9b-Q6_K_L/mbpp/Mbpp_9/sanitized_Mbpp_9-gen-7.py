def find_Rotations(s):
    if not s:
        return 0
    n = len(s)
    for i in range(1, n):
        if s[i:] + s[:i] == s:
            return i
    return n