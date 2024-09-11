def start_withp(words):
    lst = []
    for i in words:
        if i[0]=='p':
            lst.append(i)
    return (lst[0], lst[1])


# Another solution
def start_withp(words):
    return ([x for x in words if x[0] == 'p'][0],
            [x for x in words if x[0] == 'p'][1])


# Using filter function
def start_withp(words):
    return (list(filter(lambda x: x[0] == 'p', words))[0],
            list(filter(lambda x: x[0] == 'p', words))[1])

# Using lambda function with map and list
def start_withp(words):
    return (list(map(lambda x: x[0], filter(lambda x: x[0] == 'p', words)))[0],
            list(map(lambda x: x[0], filter(lambda x: x[0] == 'p', words)))[1])



"""
Another way to do it is using regular expression:
"""

import re

def start_withp(words):
    matches = re.findall(r'^p.*', words)
    if len(matches) == 0:
        return None
    elif len(matches) == 1:
        return matches[0]
    else:
        return (matches[0], matches[1])


# Using regular expression to find two words starting with 'p'
import re
def start_withp(words):
    matches = re.findall(r'^p.*', words)
    return matches


# Using regular expression to find two or more words starting with 'p'
import re
def start_withp(words):
    matches = re.findall(r'^p.*', words)
    if len(matches) < 2:
        return None
    else:
        return matches

"""
Using Python's built-in functions:
"""

def start_withp(words):
    return (list(filter(lambda x: x[0]