def find_Rotations(s):
    if len(set(s)) == 1:  # if all characters are the same, only one rotation is needed
        return 1
    for i in range(1, len(s)):
        if s[i:] + s[:i] == s:
            return i
    return -1  # if no rotation found, return -1