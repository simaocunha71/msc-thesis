def find_Rotations(str):
    count = 0
    while str != str[len(str)-1]+str[:len(str)-1]:
        str = str[len(str)-1]+str[:len(str)-1]
        count += 1
    return count