def find_Rotations(s):
    for i in range(len(s)):
        if s == s[i:] + s[:i]:
            return i
    return 0