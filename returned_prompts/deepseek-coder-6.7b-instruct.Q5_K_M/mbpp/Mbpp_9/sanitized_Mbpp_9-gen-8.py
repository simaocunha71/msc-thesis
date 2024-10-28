def find_Rotations(s: str) -> int:
    n = len(s)
    for i in range(1, n):
        if s[:i] == s[n-i:]:
            return i
    return 0