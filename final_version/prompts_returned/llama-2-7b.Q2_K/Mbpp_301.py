"""
Write a function to find the depth of a dictionary.
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
"""
from typing import List

def dict_depth(d:dict)->int :
    if not d: return 0 # base case
    
    li = list()
    def dfs(d:dict)->int :
        if not d: return len(li)
        for k in sorted(list(set([k]) | {x for x in d.keys()})):
            if d[k]:  # the value is a dict itself
                li.append((len(li), k))
                dfs(d[k]) + 1
            else:
                li.append((len(li), k))
        return len(li)
    return dfs(d)
