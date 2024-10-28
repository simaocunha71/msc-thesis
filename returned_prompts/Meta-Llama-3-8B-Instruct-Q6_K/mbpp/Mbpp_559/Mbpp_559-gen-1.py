```
def max_sub_array_sum(arr, n):
    max_sum = float('-inf')
    current_sum = 0
    for i in range(n):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum
```
Explanation:
The problem is asking to find the sum of the largest contiguous sublist in the given list. The function max_sub_array_sum takes a list of numbers and an integer n as input, where n is the size of the list.

The function initializes two variables, max_sum and current_sum, to keep track of the maximum sum and the current sum of the sublist respectively. It then iterates through the list, adding each element to the current_sum. If the current_sum exceeds max_sum, it updates max_sum. If the current_sum becomes negative, it resets it to 0.

Finally, the function returns max_sum, which is the sum of the largest contiguous sublist in the given list.

The unit test `assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7` ensures that the function works correctly. It checks that the sum of the largest contiguous sublist in the list `[-2, -3, 4, -1, -2, 1, 5, -3]` is 7, which is the correct answer.