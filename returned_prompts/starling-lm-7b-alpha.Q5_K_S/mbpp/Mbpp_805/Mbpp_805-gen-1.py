```
def max_sum_list(input_list):
    max_sum = 0
    max_list = []
    for i in range(len(input_list)):
        if max_sum < sum(input_list[i]):
            max_sum = sum(input_list[i])
            max_list = input_list[i]
    return max_list
```

Explanation:
We can solve this problem using a simple approach. We traverse through the input list and calculate the sum of each list in the input list. If the sum of a list is greater than the previous maximum sum, we update the maximum sum and maximum list. Finally, we return the maximum list which has the highest sum of elements.

In the provided code, we initialize `max_sum` and `max_list` variables to store the maximum sum and corresponding list. We iterate through the input list using a `for` loop. Inside the loop, we compare the sum of the current list with the maximum sum. If the sum of the current list is greater than the maximum sum, we update the maximum sum and maximum list. After traversing through all the lists in the input list, we return the maximum list.

The time complexity of this solution is O(n), where n is the total number of elements in the input list. The space complexity is O(1), as we only use a constant amount of extra space to store the maximum sum and maximum list.

The provided assertion `assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]` checks if the `max_sum_list` function correctly returns the maximum list based on the sum of its elements.

Overall, this solution provides a simple and efficient way to find the list in a list of lists with the highest sum of elements.

Note: The assertion is important to ensure that the `max_sum_list` function is working correctly. Without the assertion, we cannot be sure if the function is producing the correct result.

Here are some additional test cases to demonstrate the usage of the `max_sum_list` function:

```python
print(max_sum_