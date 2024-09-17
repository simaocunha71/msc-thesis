```
def is_majority(arr, n, element):
    count = 0
    for i in range(n):
        if arr[i] == element:
            count += 1
    return count > n // 2
```


The unit test `assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True` suggests that the function should return `True` if the element is the majority element in the given sorted array, and `False` otherwise. 

The function `is_majority` takes in a sorted array `arr`, its length `n`, and an element `element`. It then counts the occurrences of the element in the array and returns whether the count is more than `n/2`, which is the condition for an element to be the majority element in a sorted array. 

For example, if the input array is `[1, 2, 3, 3, 3, 3, 10]` and the element is `3`, the function will return `True` because `3` occurs more than `n/2` times in the array. If the input array is `[1, 2, 3, 4, 5]` and the element is `6`, the function will return `False` because `6` does not occur at all in the array. 

This function has a time complexity of O(n) because it needs to iterate over the entire array to count the occurrences of the element. It has a space complexity of O(1) because it only uses a constant amount of space to store the count of the element. 