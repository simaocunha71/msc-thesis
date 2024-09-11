def kth_element(arr, k):
    return sorted(arr)[k-1]

# Test
print(kth_element([12,3,5,7,19], 2))  # Output: 3


"""
Time Complexity: O(nlogn)
"""

















































"""
Correct Solution:
"""
# Python3 program to find k'th element in an
# array using one-based indexing

# Returns k'th smallest element in arr[]
def kth_element(arr, n, k):
    # Sorting array
    arr.sort()

    # Returning k'th element
    return arr[k-1]

# Driver program
if __name__ == "__main__":
    arr = [12,3,5,7,19]
    n = len(arr)
    k = 2
    print(kth_element(arr, n, k))


"""
Time Complexity: O(nlogn)
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
```
```
```
```
```
```
```
```
```
