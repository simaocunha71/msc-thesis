```
def max_sub_array_sum(arr, n):
    max_sum = float('-inf')
    current_sum = 0
    for i in range(n):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum
```
This function uses Kadane's algorithm to find the maximum sum of a contiguous sublist within the given list. The function initializes `max_sum` to negative infinity and `current_sum` to 0. It then iterates over the list, updating `current_sum` to be the maximum of the current element and the sum of the current element and the previous `current_sum`. It updates `max_sum` to be the maximum of `max_sum` and `current_sum`. Finally, it returns `max_sum`. 

The unit test `assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7` ensures that the function correctly finds the maximum sum of a contiguous sublist in the given list. In this case, the maximum sum is 7, which is the sum of the sublist [1, 5]. 

Note: The function takes two parameters: the list of numbers and the size of the list. This is because the problem statement does not specify the size of the list, so it is included as a parameter. The unit test also includes the size of the list (8) to ensure that the function works correctly. 

However, the problem statement can be interpreted as finding the maximum sum of a contiguous sublist within the given list, regardless of its size. In this case, the function can be simplified to only take one parameter, the list of numbers. The unit test can be modified to only include the list of numbers, without the size. 

Here is the simplified function and unit test:

```
def max_sub_array_sum(arr):
    max_sum = float('-inf')
    current_sum = 0
    for i in range(len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3]) == 7
```  ```python
def max_sub_array_sum(arr):
    max_sum = float('-inf')
    current_sum = 0