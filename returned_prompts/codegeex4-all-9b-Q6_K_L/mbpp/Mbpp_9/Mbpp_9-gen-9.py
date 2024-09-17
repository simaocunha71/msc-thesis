def find_Rotations(s: str) -> int:
    count = 0
    for i in range(len(s)):
        if s[i] == s[0]:
            count += 1
    return count

