def find_Rotations(inputString):
    if len(inputString) == 0:
        return 0
    for i in range(1, len(inputString)):
        if inputString[i:] + inputString[:i] == inputString:
            return len(inputString) - i
    return 0