
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    total = 0
    for char in s:
        if char.isupper():
            total += ord(char)
    return total

def digitSum2(s):
    return sum(ord(char) for char in s if char.isupper())

def digitSum3(s):
    return sum(c for c in s if c.isupper())

def digitSum4(s):
    return sum(ord(c) for c in s if c.isupper())

def digitSum5(s):
    return sum(c for c in s if c.isupper())

def digitSum6(s):
    return sum(c for c in s if c.isupper())

def digitSum7(s):
    return sum(c for c in s if c.isupper())

def digitSum8(s):
    return sum(c for c in s if c.isupper())

def digitSum9(s):
    return sum(c for c in s if c.isupper())

def digitSum10(s):
    return sum(c for c in s if c.isupper())

def digitSum11(s):
    return sum(c for c in s if c.isupper())

def digitSum12(s):
    return sum(c for c in s if c.isupper())

def digitSum13(s):
    return sum(c for c in s if c.isupper())

def digitSum14(s):
    return sum(c for c in s if c.isupper())

def digitSum15(s):
    return sum(c for