```
def is_majority(arr, n, element):
    count = 0
    for num in arr:
        if num == element:
            count += 1
    return count > n // 2
```



In this problem, we need to check if the given element is the majority element in the sorted array. The majority element is the element that occurs more than n/2 times, where n is the length of the array. 

The problem does not specify if the array is rotated or not, so we can assume it's not rotated. 

The unit test `assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True` suggests that the array is not rotated. 

We can solve this problem by counting the occurrences of the given element in the array. If the count is greater than n/2, then the element is the majority element. 

Here is the Python solution:

```
def is_majority(arr, n, element):
    count = 0
    for num in arr:
        if num == element:
            count += 1
    return count > n // 2
```

This function iterates over the array, counts the occurrences of the given element, and returns True if the count is greater than n/2, and False otherwise. 