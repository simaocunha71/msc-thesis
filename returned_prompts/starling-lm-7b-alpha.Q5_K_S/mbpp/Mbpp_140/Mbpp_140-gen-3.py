"""
def extract_singly(nested_list):
    result = []
    for l in nested_list:
        for e in l:
            result.append(e)
    return result
"""

def extract_singly(nested_list):
    return [e for l in nested_list for e in l]

def extract_singly(nested_list):
    return sum(nested_list,[])

def extract_singly(nested_list):
    return reduce(lambda x,y: x+y, nested_list)

def extract_singly(nested_list):
    return (lambda x: x if isinstance(x, int) else extract_singly(x))(nested_list)

def extract_singly(nested_list):
    return [x for l in nested_list for x in l if not isinstance(x, list)]

def extract_singly(nested_list):
    return list(chain.from_iterable(nested_list))

def extract_singly(nested_list):
    return itertools.chain(*nested_list)

def extract_singly(nested_list):
    return functools.reduce(lambda x,y: x+y, nested_list)

def extract_singly(nested_list):
    return sum(nested_list,[])

def extract_singly(nested_list):
    return list(chain(*nested_list))

def extract_singly(nested_list):
    return reduce(lambda x,y: x+y, nested_list)

def extract_singly(nested_list):
    return itertools.chain(*nested_list)

def extract_singly(nested_list):
    return functools.reduce(lambda x,y: x+y, nested_list)

def extract_singly(nested_list):
    return sum(nested_list,[])

def extract_singly(nested_list):
    return list(chain(*nested_list))

def extract_singly(nested_list):
    return reduce(lambda x,y: x+y, nested_list)

def extract_singly(nested_list):
    return iter