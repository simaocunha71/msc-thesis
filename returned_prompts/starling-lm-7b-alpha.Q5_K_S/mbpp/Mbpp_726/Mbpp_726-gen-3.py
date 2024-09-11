def multiply_elements(t):
    res = []
    for i in range(len(t)-1):
        res.append(t[i]*t[i+1])
    return tuple(res)

print(multiply_elements((1, 5, 7, 8, 10)))

# Output:
(5, 35, 56, 80)














"""
def multiply_elements(t):
    res = []
    for i in range(len(t)-1):
        res.append(t[i]*t[i+1])
    return tuple(res)
"""


"""
def multiply_elements(t):
    res = []
    for i in range(len(t)):
        if i == len(t)-1:
            res.append(t[i])
        else:
            res.append(t[i]*t[i+1])
    return tuple(res)
"""
"""
def multiply_elements(t):
    res = []
    for i in range(len(t)):
        if i == 0:
            res.append(t[i])
        else:
            res.append(t[i]*t[i-1])
    return tuple(res)
"""
"""
def multiply_elements(t):
    res = []
    for i in range(len(t)):
        if i == 0:
            res.append(t[i])
        elif i == len(t)-1:
            res.append(t[i])
        else:
            res.append(t[i]*t[i+1])
    return tuple(res)
"""
"""
def multiply_elements(t):
    res = []
    for i in range(len(t)):
        if i == 0:
            res.append(t[i])
        elif i == len(t)-1:
            res.append(t[i])
        elif i == len(t)-2:
            res.append(t[i]*t[i+1])
        else:
            res.append