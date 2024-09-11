def odd_Equivalent(s,n):
    length = len(s)
    res = 0
    for i in range(length):
        if (s[i] == "1"):
            res += 1
    for i in range(1,n+1):
        if (i%2 != 0):
            res += (res%2)
    return res

#assert odd_Equivalent("011001",6) == 3





"""

Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.

"""

def odd_Equivalent(s,n):
    length = len(s)
    res = 0
    for i in range(length):
        if (s[i] == "1"):
            res += 1
    for i in range(1,n+1):
        if (i%2 != 0):
            res += (res%2)
    return res

#assert odd_Equivalent("011001",6) == 3



"""

Given a binary string, write a python function to determine the number of times it can be rotated such that the leftmost and rightmost characters are equal.

"""

def rotate(s):
    length = len(s)
    res = 0
    for i in range(length):
        if (s[i] == s[length-1]):
            res += 1
    return res

#assert rotate("10111011") == 4

"""

Given a binary string, write a python function to determine the number of times it can be rotated such that the leftmost and rightmost characters are equal.

"""

def rotate(s):
    length = len(s)
    res = 0
    for i in range(length):
        if (s[i] == s[length-1]):
            res += 1
    return res

#assert rotate("10111011") == 4

"""

Given a binary string, write a python function to determine the