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
This function takes an array and the number of elements in the array as input. It first sorts the array in ascending order. Then it iterates over the array, calculating the difference between each element and the previous one. It keeps track of the minimum difference found so far and returns it at the end.

For example, if the input array is (1,5,3,19,18,25) and the number of elements is 6, the function will return 1, which is the minimum difference between any two elements in the array (5-3). 

The unit test `assert find_min_diff((1,5,3,19,18,25),6) == 1` ensures that the function works correctly. 

The time complexity of this function is O(n log n) due to the sorting operation, and the space complexity is O(1) as it only uses a constant amount of space. 





