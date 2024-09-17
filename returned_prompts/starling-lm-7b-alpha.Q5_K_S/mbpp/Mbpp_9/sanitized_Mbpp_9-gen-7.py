def find_Rotations(s):
    """
    Find the minimum number of rotations (greater than 0)
    required to get the same string.
    """
    for i in range(len(s)):
        if s[:i] + s[i:] == s:
            return len(s) // i
    return 0