Here is the python code for the problem.

```python
def pluck(arr):
    smallestNum = float('inf')
    smallestIndex = float('inf')

    for i in range(len(arr)):
        if arr[i] < smallestNum and arr[i] % 2 == 0:
            smallestNum = arr[i]
            smallestIndex = i

    if smallestNum == float('inf'):
        return []

    return [smallestNum, smallestIndex]
```

In this code, we first initialize smallestNum and smallestIndex to infinity. We then iterate through the array. If we find a number that is smaller than smallestNum and is even, we update smallestNum and smallestIndex. Finally, if smallestNum is still infinity, we return an empty list, otherwise we return the smallest even number and its index.

This code runs in O(n) time, where n is the length of the array.

This code works as expected for all test cases given in the problem statement.

Test cases:

print(pluck([4,2,3])) # Output: [2, 1]
print(pluck([1,2,3])) # Output: [2, 1]
print(pluck([])) # Output: []
print(pluck([5,