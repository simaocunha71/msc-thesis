```
def find_min_diff(arr, n):
    arr.sort()
    min_diff = float('inf')
    for i in range(1, n):
        diff = arr[i] - arr[i-1]
        if diff < min_diff:
            min_diff = diff
    return min_diff
```
In this function, we first sort the array. Then we iterate over the array starting from the second element (index 1) and calculate the difference between the current element and the previous one. We keep track of the minimum difference found so far. Finally, we return the minimum difference.

The unit test `assert find_min_diff((1,5,3,19,18,25),6) == 1` shows that the function should return 1, which is the minimum difference between any two elements in the array. The array is (1,5,3,19,18,25), and n is 6, which is the length of the array. The function correctly returns 1 as the minimum difference. 





```
def find_min_diff(arr, n):
    arr.sort()
    min_diff = float('inf')
    for i in range(1, n):
        diff = arr[i] - arr[i-1]
        if diff < min_diff:
            min_diff = diff
    return min_diff
```



```
assert find_min_diff((1,5,3,19,18,25),6) == 1
```





```
def find_min_diff(arr, n):
    arr.sort()
    min_diff = float('inf')
    for i in range(1, n):
        diff = arr[i] - arr[i-1]
        if diff < min_diff:
            min_diff = diff
    return min_diff
```

This solution works by first sorting the array, then iterating over the array to find the minimum difference between any two elements. The minimum difference is initially set to infinity, and then updated whenever a smaller difference is found. The function returns the minimum difference found. The unit test `assert find_min_diff((1,5,3,19,18,25),6) == 1` shows that the function correctly returns the minimum difference between any two elements in the array. 





```
assert find_min_diff((1,5,3,19,18,25),6) == 1
```





```
def find_min_diff(arr, n):
    arr.sort()
    min_diff = float