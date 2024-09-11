"""
def extract_even(t):
    if type(t) is tuple:
        return tuple(filter(lambda x: type(x) in [int, tuple] and x % 2 == 0, t))
    elif type(t) is list:
        return list(filter(lambda x: type(x) in [int, list] and x % 2 == 0, t))
    else:
        return t

print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8)))
"""

def extract_even(t):
    if isinstance(t, tuple):
        return tuple(filter(lambda x: isinstance(x, (int, tuple)) and x % 2 == 0, t))
    elif isinstance(t, list):
        return list(filter(lambda x: isinstance(x, (int, list)) and x % 2 == 0, t))
    else:
        return t

print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8)))



# 不使用过滤器
"""
def extract_even(t):
    if type(t) is tuple:
        result = []
        for item in t:
            if type(item) in [int, tuple] and item % 2 == 0:
                result.append(item)
        return tuple(result)
    elif type(t) is list:
        result = []
        for item in t:
            if type(item) in [int, list] and item % 2 == 0:
                result.append(item)
        return result
    else:
        return t

print(extract_even((4, 5, (7, 6, (2, 4)), 6, 8)))
"""


# 使用lambda表达式
"""
def extract_even(t):
    if type(t) is tuple:
        return tuple(filter(lambda x: type(x) in [int, tuple] and x % 2 == 0, t))
    elif type(t) is list:
       