
def find_Rotations(s: str) -> int:
    for i in range(1, len(s)):
        if s[i:] == s[:i]:
            return i
    return len(s)


