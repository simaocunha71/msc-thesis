def find_Rotations(s):
    rotations = 1
    while True:
        if s == s[1:] + s[0]:
            return rotations
        s = s[1:] + s[0]
        rotations += 1