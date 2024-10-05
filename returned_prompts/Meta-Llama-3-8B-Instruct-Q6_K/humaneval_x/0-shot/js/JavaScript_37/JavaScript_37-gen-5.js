Here is a Python implementation of the function:

```Python
def sortEven(l):
    return [i if i % 2 != 0 else sorted([x for x in l if x % 2 == 0])[i % 2] for i in range(len(l))]
```

This function works by iterating over the list `l` and checking if the index `i` is odd or even. If `i` is odd, the function simply returns the value at index `i` from the original list `l`. If `i` is even, the function returns the value at index `i % 2` from the sorted list of even values, which is obtained by using a list comprehension to filter out the even values from `l` and then sorting them. 

For example, if you call `sortEven([1, 2, 3])`, the function will return `[1, 2, 3]` because the even index (1) is already sorted. If you call `sortEven([5, 6, 3, 4])`, the function will return `[3, 6, 5, 4]`, because the even index (1) is equal to 6, which is the second smallest even value in the list. The odd indices (0 and 2) remain unchanged. 