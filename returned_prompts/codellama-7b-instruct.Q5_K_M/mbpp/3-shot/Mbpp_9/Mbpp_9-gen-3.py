
def find_Rotations(str1):
    return len(str1) - str1.find(str1[::-1]) - 1


