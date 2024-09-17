def odd_Equivalent(s, rotations):
    count = 0
    for _ in range(rotations):
        s = s[1:] + s[0]
    for i in range(len(s)):
        if int(s[i]) % 2 != 0:
            count += 1
    return count