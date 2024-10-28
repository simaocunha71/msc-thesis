def find_Rotations(s):
    min_rot = float('inf')
    for i in range(1, len(s)):
        if s == s[i:] + s[:i]:
            min_rot = min(min_rot, i)
    return min_rot if min_rot != float('inf') else 0