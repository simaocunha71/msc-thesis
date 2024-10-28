def find_Rotations(string):
    count = 0
    while string != string[::-1]:
        string = string[1:] + string[0]
        count += 1
    return count