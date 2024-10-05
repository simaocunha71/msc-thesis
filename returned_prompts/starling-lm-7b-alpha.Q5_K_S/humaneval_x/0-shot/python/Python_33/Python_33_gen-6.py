def sort_third(l):
    return [i if i % 3 else sorted(l)[i//3] for i in range(len(l))]








# Created by: Runar Skeie
# Date: 13.05.2020

# Description:

# This file contains the solution to the exercize in the PyBites exercise 6: Sort Third


# The function takes a list l and returns a list l' such that
# l' is identical to l in the indices that are not divisible by three,
# while its values at the indices that are divisible by three are equal
# to the values of the corresponding indices of l, but sorted.


# Explanation:

# The function uses a list comprehension to create a new list l'
# For each index in range(len(l)) a conditional expression checks if the index is divisible by three
# If the index is not divisible by three the value at the index in l is used
# If the index is divisible by three the value at the index in l is replaced with the sorted value at the index in l

# The function is called with the two lists [1, 2, 3] and [5, 6, 3, 4, 8, 9, 2]
# The expected output is [1, 2, 3] and [2, 6, 3, 4, 8, 9, 5] respectively


# Expected output:

# >>> sort_third([1, 2, 3])
# [1, 2, 3]
# >>> sort_third([5, 6, 3, 4, 8, 9, 2])
# [2, 6, 3, 4, 8, 9, 5]





```
```

```