"""
def extract_singly(l):
    # your code here
    result = []
    for sub_list in l:
        for item in sub_list:
            result.append(item)
    return set(result)
"""

def extract_singly(l):
    # your code here
    return set(item for sub_list in l for item in sub_list)

def extract_singly(l):
    return set(item for sub_list in l for item in sub_list)

def extract_singly(l):
    return set.union(*l)

def extract_singly(l):
    return reduce(set.union, l)

def extract_singly(l):
    return set(reduce(lambda a,b: a+b, l))

def extract_singly(l):
    return set(reduce(lambda a,b: a.union(b), l))




"""
def extract_singly(l):
    result = []
    for sub_list in l:
        for item in sub_list:
            result.append(item)
    return set(result)

def extract_singly(l):
    result = []
    for sub_list in l:
        for item in sub_list:
            result.append(item)
    return set(result)

def extract_singly(l):
    result = []
    for sub_list in l:
        for item in sub_list:
            result.append(item)
    return set(result)

def extract_singly(l):
    result = []
    for sub_list in l:
        for item in sub_list:
            result.append(item)
    return set(result)

def extract_singly(l):
    result = []
    for sub_list in l:
        for item in sub_list:
            result.append(item)
    return set(result)

def extract_singly(l):
    result = []
    for sub_list in l:
        for item in sub_list:
            result.append(item)
    return set(result)
