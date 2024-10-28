def odd_Equivalent(s: str, num_rotations: int) -> int:
    count = 0
    for i in range(len(s)):
        rotated_str = s[i:] + s[:i]
        if int(rotated_str, 2) % 2 != 0:
            count += 1
    return count