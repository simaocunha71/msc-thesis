def odd_Equivalent(s, rotations):
    count = 0
    for _ in range(rotations):
        s = s[1:] + s[0]
    for char in s:
        if char == '1':
            count += 1
    return count