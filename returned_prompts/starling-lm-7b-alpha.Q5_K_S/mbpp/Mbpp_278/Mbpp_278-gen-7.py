def count_first_elements(t):
    count = 0
    for i in t:
        if isinstance(i, tuple):
            for j in i:
                count += 1
        else:
            count += 1
    return count

print(count_first_elements((1, 5, 7, (4, 6), 10) ))






"""
def count_first_elements(t):
    count = 0
    for i in t:
        if isinstance(i, tuple):
            count += len(i)
        else:
            count += 1
    return count

print(count_first_elements((1, 5, 7, (4, 6), 10) ))
"""


"""
def count_first_elements(t):
    return len(t)-len([i for i in t if isinstance(i, tuple)])

print(count_first_elements((1, 5, 7, (4, 6), 10) ))
"""

"""
def count_first_elements(t):
    return sum(1 for i in t if isinstance(i, tuple))

print(count_first_elements((1, 5, 7, (4, 6), 10) ))
"""

"""
def count_first_elements(t):
    return sum(1 for i in t if isinstance(i, tuple))

print(count_first_elements((1, 5, 7, (4, 6), 10) ))
"""

"""
def count_first_elements(t):
    count = 0
    for i in t:
        if isinstance(i, tuple):
            count += 1
            for j in i:
                count += 1
        else:
            count += 1
    return count

print(count_first_elements((1, 5, 7, (4, 6), 10) ))
"""


"""
def count_first_elements(t):
    count = 0
    for i in t:
        if isinstance(i, tuple):
            for j in i