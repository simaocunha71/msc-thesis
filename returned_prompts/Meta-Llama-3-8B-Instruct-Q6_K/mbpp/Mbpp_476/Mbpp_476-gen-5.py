```
def big_sum(arr):
    return sum(sorted(arr)[0:2])
```


The function `big_sum` takes an array `arr` as an argument, sorts it in ascending order, and returns the sum of the first and the last element of the sorted array. The unit test `assert big_sum([1,2,3]) == 4` ensures that the function works correctly. The sum of the largest and smallest value in the array [1,2,3] is 1+3=4. The function will pass this test. 

However, the problem statement asks to find the sum of the largest and smallest value in the array, not the sum of the first and the last element of the sorted array. This difference is crucial and must be considered while solving the problem. 

Here's the corrected code:
```
def big_sum(arr):
    return max(arr) + min(arr)
```
This function directly calculates the sum of the maximum and minimum values in the array. It will pass the unit test `assert big_sum([1,2,3]) == 4`. 
The time complexity of this function is O(n log n) due to the max and min functions, where n is the number of elements in the array. If the array is already sorted, the time complexity would be O(n) with a different approach. 