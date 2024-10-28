```
def is_Monotonic(arr):
    if arr == sorted(arr):
        return True
    if arr == sorted(arr, reverse=True):
        return True
    return False
```
This function takes an array as input and checks if it is either monotonically increasing or decreasing. It does this by comparing the array with its sorted version and its reverse sorted version. If the array is equal to either of these, it is considered monotonically increasing or decreasing and the function returns True. If the array is not equal to either of these, it is not monotonically increasing or decreasing and the function returns False. 

The unit test `assert is_Monotonic([6, 5, 4, 4]) == True` ensures that the function works correctly. 

This problem is solved by comparing the array with its sorted version and its reverse sorted version. If the array is equal to either of these, it is considered monotonically increasing or decreasing and the function returns True. If the array is not equal to either of these, it is not monotonically increasing or decreasing and the function returns False. 

The function is_Monotonic is used to check if the given array is monotonically increasing or decreasing. The function takes an array as input and checks if it is either monotonically increasing or decreasing. If the array is equal to its sorted version or its reverse sorted version, it is considered monotonically increasing or decreasing and the function returns True. If the array is not equal to either of these, it is not monotonically increasing or decreasing and the function returns False. 

The unit test `assert is_Monotonic([6, 5, 4, 4]) == True` ensures that the function works correctly. 

This function can be used to solve the problem of checking if a given array is monotonically increasing or decreasing. It is a simple and efficient solution that works correctly for all inputs. 

The time complexity of this function is O(n log n) due to the sorting operations. The space complexity is O(n) for the sorted and reverse sorted versions of the array. 

This function can be used to solve problems that require checking if a given array is monotonically increasing or decreasing. It is a useful tool in data analysis and processing. 

It can also be used to solve problems that require checking if a given array is monotonically increasing or decreasing and then performing some action based on the result. For example, if