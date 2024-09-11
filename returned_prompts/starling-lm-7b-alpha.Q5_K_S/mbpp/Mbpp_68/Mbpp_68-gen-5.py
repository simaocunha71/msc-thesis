"""
def is_Monotonic(l):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            return False
    return True


def is_Monotonic(l):
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(l[i] >= l[i + 1] for i in range(len(l) - 1))

def is_Monotonic(l):
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(l[i] >= l[i + 1] for i in range(len(l) - 1))

def is_Monotonic(l):
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(l[i] >= l[i + 1] for i in range(len(l) - 1))

def is_Monotonic(l):
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(l[i] >= l[i + 1] for i in range(len(l) - 1))
"""

def is_Monotonic(l):
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or all(l[i] >= l[i + 1] for i in range(len(l) - 1))


# assert(is_Monotonic([1, 2, 3, 4, 5]) == True)
# assert(is_Monotonic([6, 5, 4, 4]) == True)
# assert(is_Monotonic([6, 5, 4, 5]) == True)
# assert(is_Monotonic([6, 5, 4, 3]) == False)
# assert(is_Monotonic([6, 5, 3