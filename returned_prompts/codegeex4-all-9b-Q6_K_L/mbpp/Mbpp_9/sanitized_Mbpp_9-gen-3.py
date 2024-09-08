def find_Rotations(s):
    if len(s) == 1:
        return 1
    for i in range(1, len(s)):
        if s[i:] + s[:i] == s:
            return i
    return -1