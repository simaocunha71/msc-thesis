
def find_Rotations(str):
    if len(str) == 0:
        return 0
    for i in range(len(str)):
        if str == str[i:]+str[:i]:
            return len(str) - i
    return len(str)


