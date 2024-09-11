"""
def find_Rotations(inputString):
    if len(inputString) == 0:
        return 0
    for i in range(len(inputString)):
        if inputString[i:] + inputString[:i] == inputString:
            return len(inputString) - i
    return 0
"""

def find_Rotations(inputString):
    if len(inputString) == 0:
        return 0
    for i in range(1, len(inputString)):
        if inputString[i:] + inputString[:i] == inputString:
            return len(inputString) - i
    return 0

print(find_Rotations("aaaa"))  # 1
print(find_Rotations("abcd"))  # 2
print(find_Rotations(""))  # 0

```