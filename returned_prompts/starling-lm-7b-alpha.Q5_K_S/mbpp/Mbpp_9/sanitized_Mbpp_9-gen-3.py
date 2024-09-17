def find_Rotations(s):
    if len(s) == 1:
        return 0
    else:
        for i in range(len(s)):
            if s[:i] == s[i:]:
                return i + 1