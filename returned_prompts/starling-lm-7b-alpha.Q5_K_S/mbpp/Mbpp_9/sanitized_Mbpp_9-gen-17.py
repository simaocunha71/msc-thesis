def find_Rotations(s: str):
    if len(s) == 1:
        return 0
    else:
        n = len(s)
        if s[:n//2] == s[n//2:]:
            return 0
        else:
            return n//2 + 1