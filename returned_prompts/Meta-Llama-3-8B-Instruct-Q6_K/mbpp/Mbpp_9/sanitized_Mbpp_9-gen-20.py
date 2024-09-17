def find_Rotations(s):
    rotations = 0
    for i in range(1, len(s)):
        if s == s[i:] + s[:i]:
            return i
    return len(s)