def find_Rotations(str):
    if len(str) == 1:
        return 0
    else:
        for i in range(len(str)):
            if str[-1] == str[0]:
                return 1 + find_Rotations(str[1:])
        return 0