def find_Rotations(s):
    if not s:
        return 0
    for i in range(1, len(s)):
        if s == s[i:] + s[:i]:
            return i
    return -1