"""
Write a function to check if given tuple contains no duplicates.
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
"""

def check_distinct(tup):
    seen = set()
    
    for each in tup:
        if each not in seen:
            seen.add(each)
        elif each in seen: # we know this element is distinct
            return True
        
    return False