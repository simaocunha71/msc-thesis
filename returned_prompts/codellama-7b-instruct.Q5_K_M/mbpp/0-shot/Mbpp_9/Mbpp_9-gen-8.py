def find_Rotations(str):
    count = 0
    for i in range(1, len(str)):
        if str[:i] == str[i:]:
            count += 1
    return count
