def find_Rotations(s: str) -> int:
    """Find the minimum number of rotations required to get the same string."""
    for i in range(1, len(s)):
        if s[i:] + s[:i] == s:
            return i
    return -1  # If no rotations are possible