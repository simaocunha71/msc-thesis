def find_Rotations(s):
    def rotations(s):
        for i in range(1, len(s)):
            yield s[i:] + s[:i]

    min_rotations = float('inf')
    for rotation in rotations(s):
        if rotation == s:
            min_rotations = min(min_rotations, i + 1)
    return min_rotations if min_rotations != float('inf') else None