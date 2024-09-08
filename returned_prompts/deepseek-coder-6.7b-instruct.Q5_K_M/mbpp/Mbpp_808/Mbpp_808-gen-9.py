def check_K(tup, k):
    return k in tup

print(check_K((10, 4, 5, 6, 8), 6))  # True

# OR

def check_K(tup, k):
    return any(i == k for i in tup)

print(check_K((10, 4, 5, 6, 8), 6))  # True

# OR

def check_K(tup, k):
    if k in tup:
        return True
    else:
        return False

print(check_K((10, 4, 5, 6, 8), 6))  # True

# OR

def check_K(tup, k):
    for i in tup:
        if i == k:
            return True
    return False

print(check_K((10, 4, 5, 6, 8), 6))  # True

"""
All of these will return True if the tuple contains the value of "k", and False if not.
"""
<jupyter_output>
True
True
True
True
True
<jupyter_text>
3. Create a function named "reverse_tuple" that takes a tuple and returns the reverse of that tuple.
<jupyter_code>
