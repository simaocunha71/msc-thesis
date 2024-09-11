"""
def test_duplicate(arr):
    return len(set(arr)) != len(arr)
"""

# Alternative solution
def test_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

# Test
print(test_duplicate([1,2,3,4,5])) # True
print(test_duplicate([1,2,3,3,4,5])) # True
print(test_duplicate([1,2,3,4,5,6])) # False

# Time: O(n^2)
# Space: O(1)


"""
In the provided solution, the time complexity is O(n^2) because there are two nested loops that iterate over the entire array.
The space complexity is O(1) because no additional data structures are used to store the elements.

In the alternative solution, the time complexity is also O(n^2) because there are two nested loops that iterate over the entire array. However, the space complexity is O(1) because no additional data structures are used to store the elements.
"""

```
```