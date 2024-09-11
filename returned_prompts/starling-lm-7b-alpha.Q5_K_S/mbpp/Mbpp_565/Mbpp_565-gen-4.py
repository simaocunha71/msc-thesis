"""
def split(s):
    lst = []
    for i in s:
        lst.append(i)
    return lst
"""

"""
def split(s):
    return [i for i in s]
"""

def split(s):
    return list(s)

assert split('python') == ['p','y','t','h','o','n']




