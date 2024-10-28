```
def is_majority(arr, n, element):
    count = 0
    for num in arr:
        if num == element:
            count += 1
    return count > n // 2
```


The function `is_majority` checks if the given element is the majority element in the sorted array. It does this by counting the occurrences of the element in the array and then checking if the count is greater than n/2. If it is, the function returns `True`, otherwise it returns `False`. The unit test `assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True` ensures that the function works correctly. This function has a time complexity of O(n), where n is the length of the array. This is because it needs to iterate over the entire array to count the occurrences of the element. The space complexity is O(1), as it only uses a constant amount of space to store the count and the element. 