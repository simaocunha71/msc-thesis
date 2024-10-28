def find_Rotations(s):
    for i in range(1, len(s)):
        if s == s[i:] + s[:i]:
            return i
    return 0