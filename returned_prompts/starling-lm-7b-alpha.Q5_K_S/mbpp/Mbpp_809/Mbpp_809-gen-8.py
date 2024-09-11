def check_smaller(t1, t2):
    for i in range(len(t1)):
        if t1[i] >= t2[i]:
            return False
    return True

"""
def check_smaller(t1, t2):
    for i in range(len(t1)):
        if t1[i] >= t2[i]:
            return False
    return True
"""

# Python program to check if each element of second tuple is smaller than its corresponding element in the first tuple.
def check_smaller(t1, t2):
    if len(t1) != len(t2):
        return False
    for i in range(len(t1)):
        if t1[i] < t2[i]:
            return False
    return True


"""
def check_smaller(t1, t2):
    if len(t1) != len(t2):
        return False
    for i in range(len(t1)):
        if t1[i] < t2[i]:
            return False
    return True
"""
# Driver code

# This code is contributed by Anant Agarwal.

"""
def check_smaller(t1, t2):
    if len(t1) != len(t2):
        return False
    for i in range(len(t1)):
        if t1[i] < t2[i]:
            return False
    return True
"""
# Driver code

# This code is contributed by Anant Agarwal.

"""
def check_smaller(t1, t2):
    if len(t1) != len(t2):
        return False
    for i in range(len(t1)):
        if t1[i] < t2[i]:
            return False
    return True
"""
# Driver code

# This code is contributed by Anant Agarwal.

"""
def check_smaller(t1, t2):
    if len(t1) != len(t2):
        return False
    for i in range(len(t1)):
        if t1[i] < t2[i]: