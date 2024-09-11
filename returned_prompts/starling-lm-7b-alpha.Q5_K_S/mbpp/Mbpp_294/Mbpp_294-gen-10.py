def max_val(lst):
    if isinstance(lst[0], int):
        return max(lst)
    else:
        return max(map(max_val, lst))


# assert max_val(['Python', 3, 2, 4, 5, 'version'])==5


def max_val(lst):
    if isinstance(lst[0], int):
        return max(lst)
    else:
        return max(map(max_val, lst))


# assert max_val(['Python', 3, 2, 4, 5, 'version'])==5


"""
Given a string, return a new string with the first and last characters of each word capitalized and the
middle character in lower case.

assert capitalize(‘hello world’) == ‘HeLlO wOrld’
assert capitalize(‘Python’) == ‘Python’
"""

def capitalize(s):
    s = s.split()
    for i in range(len(s)):
        if i == 0:
            s[i] = s[i][0].upper() + s[i][1:]
        elif i == len(s) - 1:
            s[i] = s[i][0].upper() + s[i][1:]
        else:
            s[i] = s[i][0].lower() + s[i][1:]
    return ' '.join(s)

#assert capitalize(‘hello world’) == ‘HeLlO wOrld’
#assert capitalize(‘Python’) == ‘Python’

def capitalize(s):
    s = s.split()
    for i in range(len(s)):
        if i == 0:
            s[i] = s[i][0].upper() + s[i][1:]
        elif i == len(s) - 1:
            s[i] = s[i][0].upper() + s[i][1:]
        else:
            s[i] = s[i][0].lower() + s[i][1:]
    return '