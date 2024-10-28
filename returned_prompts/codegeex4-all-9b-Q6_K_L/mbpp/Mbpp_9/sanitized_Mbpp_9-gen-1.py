def find_Rotations(s):
    min_rotations = float('inf')
    for i in range(1, len(s)):
        rotated_string = s[i:] + s[:i]
        if rotated_string == s:
            min_rotations = min(min_rotations, i)
    return min_rotations