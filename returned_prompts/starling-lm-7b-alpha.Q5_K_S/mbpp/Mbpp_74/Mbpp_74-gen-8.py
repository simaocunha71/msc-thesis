def is_samepatterns(a, b):
    if len(a) != len(b):
        return False
    else:
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True

# print(is_samepatterns(["red","green","green"], ["a", "b", "b"]))
# print(is_samepatterns(["red","green"], ["a", "b"]))
"""
def is_samepatterns(a, b):
    if len(a) != len(b):
        return False
    else:
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True

def is_samepatterns(a, b):
    if len(a) != len(b):
        return False
    else:
        if len(a) == 0:
            return True
        if a[0] != b[0]:
            return False
        if len(a) == 1:
            return True
        if a[1] == b[0]:
            return False
        if len(a) == 2:
            return True
        if a[2] == b[1]:
            return False
        if len(a) == 3:
            return True
        if a[3] == b[2]:
            return False
        if len(a) == 4:
            return True
        if a[4] == b[3]:
            return False
        if len(a) == 5:
            return True
        if a[5] == b[4]:
            return False
        if len(a) == 6:
            return True
        if a[6] == b[5]:
            return False
        if len(a) == 7:
            return True
        if a[7] == b[6]:
            return False
        if len(a) == 8:
            return True
        if a[8] == b[7]:
            return False
        if len(a) == 9:
            return True
        if a[9