```
def is_majority(sorted_array, n, element):
    return sorted_array.count(element) > n / 2
```


The unit test `assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True` suggests that the function should return `True` if the element occurs more than `n/2` times in the array. 

The function `is_majority` takes three parameters: the sorted array, its length `n`, and the element to check. It uses the built-in `count` method of Python lists to count the occurrences of the element in the array, and returns `True` if the count is greater than `n/2`, and `False` otherwise. 

This function is inefficient because it needs to iterate through the entire array for each element. However, it is simple and works correctly for the given unit test. 

Note: The Boyer-Moore Voting Algorithm can be used to solve this problem in O(n) time complexity, but it is more complex to implement. 

Here's how you could implement the Boyer-Moore Voting Algorithm:

```
def is_majority(sorted_array, n, element):
    count = 0
    for num in sorted_array:
        if num == element:
            count += 1
        else:
            count -= 1
        if count == 0:
            element = num
            count = 1
    return sorted_array.count(element) > n / 2
``` 

This function iterates through the array at most twice, once to find the majority element and once to count its occurrences. It is more efficient than the previous function, but still not optimal. 

The optimal solution would be to use the Boyer-Moore Voting Algorithm to find the majority element in O(n) time complexity, and then check its count in O(1) time complexity. This can be done using the following function:

```
def is_majority(sorted_array, n, element):
    count = 0
    candidate = None
    for num in sorted_array:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1
    return sorted_array.count(candidate) > n / 2
``` 

This function is more efficient and correct, but also more complex to implement.