def find_Rotations(s):
    rotations = 0
    for i in range(len(s)):
        if s[i:] + s[:i] == s:
            rotations = i+1
            break
    return rotations

