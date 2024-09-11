def count_charac(s):
    return len(s)

print(count_charac("python programming"))



"""
O(n)
"""


"""
def count_charac(s):
    count = 0
    for i in s:
        count += 1
    return count
"""


"""
def count_charac(s):
    return sum(1 for i in s)
"""

"""
def count_charac(s):
    return reduce(lambda count,i:count+1,s,0)
"""

"""
def count_charac(s):
    return len(set(s))
"""


"""
def count_charac(s):
    count = 0
    while s:
        count += 1
        s = s[1:]
    return count
"""


"""
def count_charac(s):
    count = 0
    while s:
        count += 1
        s = s[:-1]
    return count
"""


"""
def count_charac(s):
    count = 0
    while s:
        count += 1
        s = s[:-2]
    return count
"""


"""
def count_charac(s):
    count = 0
    while s:
        count += 1
        s = s[:len(s)-1]
    return count
"""


"""
def count_charac(s):
    count = 0
    while s:
        count += 1
        s = s[:len(s)-2]
    return count
"""


"""
def count_charac(s):
    count = 0
    while s:
        count += 1
        s = s[:len(s)-len(s)-1]
    return count
"""


"""
def count_charac(s):
    count = 0
    while s:
        count += 1
        s = s[:len(s)-len(s)-len(s)-1]
    return count
"""


"""
def count_charac(s):
   