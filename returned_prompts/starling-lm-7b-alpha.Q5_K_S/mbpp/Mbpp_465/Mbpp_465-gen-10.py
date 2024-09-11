"""
def drop_empty(dictionary):
    for k,v in dictionary.items():
        if v == None:
            del dictionary[k]
    return dictionary
"""

# Python3 program to remove all empty
# dictionaries from a list of dictionaries

def drop_empty(d):
    while