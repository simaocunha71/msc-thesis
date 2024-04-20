"""
Write a python function to remove odd numbers from a given list.
assert remove_odd([1,2,3]) == [2]
"""

def remove_odd(l):
    res = []
    
    for i in l:
        if i % 2:
            res.append(i) # add to result
        
        else:
            pass # don't change the order of items
            
    return res