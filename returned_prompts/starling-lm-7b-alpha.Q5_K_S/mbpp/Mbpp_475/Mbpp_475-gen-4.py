"""
def sort_counter(d):
    """Sort a dictionary by value."""
    return sorted(d.items(), key=lambda x:x[1])
"""

# Python program to sort a dictionary by value
def sort_dict(d):
    return sorted(d.items(), key=lambda kv: (kv[1], kv[0]))

print(sort_dict({'Math':81, 'Physics':83, 'Chemistry':87}))



# Python program to sort a dictionary by value
from operator import itemgetter
def sort_dict(d):
    return sorted(d.items(), key=itemgetter(1))

print(sort_dict({'Math':81, 'Physics':83, 'Chemistry':87}))

# Python program to sort a dictionary by value
def sort_dict(d):
    return sorted(d.items(), key=lambda kv: kv[1])

print(sort_dict({'Math':81, 'Physics':83, 'Chemistry':87}))

# Python program to sort a dictionary by value
def sort_dict(d):
    return sorted(d.items(), key=lambda x:x[1])

print(sort_dict({'Math':81, 'Physics':83, 'Chemistry':87}))

# Python program to sort a dictionary by value
def sort_dict(d):
    return sorted(d.items(), key=lambda kv: kv[1])

print(sort_dict({'Math':81, 'Physics':83, 'Chemistry':87}))

# Python program to sort a dictionary by value
def sort_dict(d):
    return sorted(d.items(), key=lambda kv: kv[1])

print(sort_dict({'Math':81, 'Physics':83, 'Chemistry':87}))

# Python program to sort a dictionary by value
def sort_dict(d):
    return sorted(d.items(), key=lambda kv: kv[1])

print(sort_dict({'Math':81, 'Physics':83, 'Chemistry':87