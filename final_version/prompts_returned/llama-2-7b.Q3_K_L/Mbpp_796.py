"""
Write function to find the sum of all items in the given dictionary.
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
"""
def return_sum(d):
    total = 0
    for key, val in d.items():
        # sum all the values
        total += val
    return total

def find_max(d, k):
    """Write a function that finds the maximum value of an item in a dictionary.
     assert find_max({'a': 100,'b':200,'c':300}) == 'c'
         or 100
        or 200
        """
    for key, val in d.items():
        if k == "a":
            return val
        elif k == "b":
            return val
        else:
            return max(d[key])

def find_min(d, k):
    """Write a function that finds the minimum value of an item in a dictionary.
     assert find_max({'a': 100,'b':200,'c':300}) == 'a'
        or 0
         or 200
        """
    for key, val in d.items():
        if k == "a":
            return min(d[key])
        elif k == "b":
            return min(d[key])
        else:
            return max(d[key])
