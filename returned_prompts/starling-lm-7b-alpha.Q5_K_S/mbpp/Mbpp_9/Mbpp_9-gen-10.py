
def find_Rotations(s):
    i = len(s)
    while i > 0:
        if s == s[i:] + s[:i]:
            return i
        i -= 1
    return 0


