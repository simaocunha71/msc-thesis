
def check_none(tup):
    for i in tup:
        if i is None:
            return True
    return False

print(check_none((10, 4, 5, 6, None)))

# Alternatively, we can use any() function which returns True if any item in the iterable is true.

def check_none(tup):
    return any(i is None for i in tup)

print(check_none((10, 4, 5, 6, None)))

# Alternatively, we can use the in operator which checks if a value is in a list.

def check_none(tup):
    return None in tup

print(check_none((10, 4, 5, 6, None)))

# Alternatively, we can use the count() method to count the number of occurrences of an element in a tuple.

def check_none(tup):
    return tup.count(None) > 0

print(check_none((10, 4, 5, 6, None)))
<jupyter_output>
True
True
True
True
<jupyter_text>
