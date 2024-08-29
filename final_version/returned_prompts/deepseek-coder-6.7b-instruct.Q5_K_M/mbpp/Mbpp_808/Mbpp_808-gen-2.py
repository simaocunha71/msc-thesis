def check_K(tup, k):
    return k in tup

print(check_K((10, 4, 5, 6, 8), 6))  # True

# 2nd Method
def check_K(tup, k):
    return any(i == k for i in tup)

print(check_K((10, 4, 5, 6, 8), 6))  # True

"""
In the first method, the 'in' operator is used to check if an item exists in a list or not.
In the second method, the 'any' function is used to check if any item in the list satisfies the condition or not.
"""

# 3rd Method
def check_K(tup, k):
    if k in tup:
        return True
    else:
        return False

print(check_K((10, 4, 5, 6, 8), 6))  # True

