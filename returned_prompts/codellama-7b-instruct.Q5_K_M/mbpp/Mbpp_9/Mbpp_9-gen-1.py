"""
def find_Rotations(str):
    if len(str) == 0:
        return 0
    else:
        for i in range(1, len(str)):
            if str[:i] == str[i:]:
                return len(str) - i
        return 1
"""
