"""
def comb_sort(lst):
    n = len(lst)
    gap = n
    swapped = True
    while gap != 1 or swapped:
        gap = gap//2
        swapped = False
        for i in range(n-gap):
            if lst[i] > lst[i+gap]:
                lst[i], lst[i+gap] = lst[i+gap], lst[i]
                swapped = True
    return lst

def test_comb_sort():
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]

test_comb_sort()
"""

def comb_sort(lst):
    n = len(lst)
    gap = n + 1
    swapped = True
    while gap != 1 or swapped:
        gap = gap//2
        swapped = False
        for i in range(n-gap):
            if lst[i] > lst[i+gap]:
                lst[i], lst[i+gap] = lst[i+gap], lst[i]
                swapped = True
    return lst

def test_comb_sort():
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]

test_comb_sort()


# Complexity
# Time: O(nlogn)
# Space: O(1)

# Reference
# https://en.wikipedia.org/wiki/Comb_sort
# Implementation in Python: https://www.geeksforgeeks.org/comb-sort/
"""

"""

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

