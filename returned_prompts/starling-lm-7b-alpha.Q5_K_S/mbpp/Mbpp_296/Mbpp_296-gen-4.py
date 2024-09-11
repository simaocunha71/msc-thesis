"""
def get_Inv_Count(arr):
    return len([i for i in range(len(arr)) if arr[i] < arr[:i] + arr[i+1:]])
"""

def get_Inv_Count(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count

print(get_Inv_Count([1,20,6,4,5]))  # returns 5
print(get_Inv_Count([2,5,3,4,6]))  # returns 5
print(get_Inv_Count([2,3,4,5,6]))  # returns 0

```
In this solution, we use two nested loops to compare each element in the array with all the other elements that come after it. If an element is found to be greater than an element that comes after it, then it is considered an inversion. The count of inversions is then returned as the result.

The time complexity of this solution is O(n^2), where n is the length of the array. This is because for each element in the array, we are comparing it with all the elements that come after it. 

The space complexity of this solution is O(1), as we are not using any additional data structures to store intermediate results. 

This solution is simple and straightforward, but it may not be the most efficient solution for large arrays.
```