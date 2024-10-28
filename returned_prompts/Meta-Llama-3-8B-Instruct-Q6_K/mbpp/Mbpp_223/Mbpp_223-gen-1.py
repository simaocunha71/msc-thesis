```
def is_majority(arr, n, element):
    count = 0
    for i in range(n):
        if arr[i] == element:
            count += 1
    return count > n // 2
```


This problem is about checking if a given element is the majority element in a sorted array. The majority element is the element that occurs more than n/2 times, where n is the length of the array.

The function is_majority takes in three parameters: the sorted array, its length, and the element to be checked. It initializes a count variable to 0 and then iterates over the array. For each element in the array, it increments the count if the element matches the given element. Finally, it returns whether the count is greater than n/2.

The unit test `assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True` ensures that the function works correctly. It checks if the element 3 is the majority element in the given array, which has a length of 7. Since 3 occurs more than 7/2 times in the array, the function should return True.