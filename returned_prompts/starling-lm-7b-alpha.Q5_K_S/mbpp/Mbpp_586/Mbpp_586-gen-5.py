def split_Arr(arr, n):
    left_part = arr[:n]
    right_part = arr[n:]
    return right_part + left_part

# Test Case
print(split_Arr([12,10,5,6,52,36],2))  # [5,6,52,36,12,10]


# Another Approach
def split_Arr(arr, n):
    return arr[n:] + arr[:n]

# Test Case
print(split_Arr([12,10,5,6,52,36],2))  # [5,6,52,36,12,10]


# Using list.insert()
def split_Arr(arr, n):
    arr.insert(0, arr.pop(n))
    return arr

# Test Case
print(split_Arr([12,10,5,6,52,36],2))  # [5,6,52,36,12,10]


# Using list.extend()
def split_Arr(arr, n):
    arr1, arr2 = arr[:n], arr[n:]
    arr2.extend(arr1)
    return arr2

# Test Case
print(split_Arr([12,10,5,6,52,36],2))  # [5,6,52,36,12,10]


# Using list slicing
def split_Arr(arr, n):
    return arr[n:] + arr[:n]

# Test Case
print(split_Arr([12,10,5,6,52,36],2))  # [5,6,52,36,12,10]


"""
To split the array at the nth element and add the first part to the end,
we can follow these approaches:

1. Using list slicing.
2. Using list.insert() method.
3. Using list.extend() method.
4. Using list concatenation.
"""

# Using list concatenation