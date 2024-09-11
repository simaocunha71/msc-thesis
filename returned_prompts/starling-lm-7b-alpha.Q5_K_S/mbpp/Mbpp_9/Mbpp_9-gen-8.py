"""
def find_Rotations(string):
    length = len(string)
    for i in range(1,length):
        if string[:i] == string[-i:]:
            return i
    return length
"""

def find_Rotations(string):
    length = len(string)
    for i in range(1,length):
        if string[:i] == string[-i:]:
            return i
    return length

print(find_Rotations("aaaa"))

"""
"""
def find_Rotations(string):
    length = len(string)
    for i in range(1,length):
        if string[:i] == string[-i:]:
            return i
    return length

print(find_Rotations("aaaa"))
"""


def find_Rotations(string):
    length = len(string)
    for i in range(1,length):
        if string[:i] == string[-i:]:
            return i
    return length

print(find_Rotations("aaaa"))

```