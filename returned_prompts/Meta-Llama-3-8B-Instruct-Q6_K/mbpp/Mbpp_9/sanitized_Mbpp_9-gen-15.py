def find_Rotations(s):
    rotations = 0
    while True:
        if s == s[1:] + s[0]:
            return rotations + 1
        s = s[1:] + s[0]
        rotations += 1