```
def max_sub_array_sum(numbers, target):
    max_sum = 0
    for i in range(len(numbers)):
        curr_sum = 0
        for j in range(i, len(numbers)):
            curr_sum += numbers[j]
            if curr_sum == target:
                max_sum = max(max_sum, curr_sum)
    return max_sum
```

Here is a Python function to solve the problem. It uses two nested loops to iterate through all possible subarrays, updating the maximum sum found so far.

The function `max_sub_array_sum` takes a list of numbers `numbers` and a target sum `target` as input. It initializes a variable `max_sum` to 0, which will store the maximum sum found.

Then, it iterates through the `numbers` list using the outer loop variable `i`. For each `i`, it initializes a variable `curr_sum` to 0, which will store the sum of the current subarray.

Inside the outer loop, there is another loop using the variable `j`, which iterates from the current index `i` to the end of the `numbers` list. This inner loop calculates the sum of the subarray from index `i` to index `j`.

If the `curr_sum` is equal to the `target`, it means that the current subarray sum is equal to the target. In this case, the function updates the `max_sum` by taking the maximum of the current `max_sum` and the `curr_sum`. This ensures that the `max_sum` will always store the maximum sum found so far.

After the inner loop finishes, the function continues to the next iteration of the outer loop, updating the `curr_sum` and checking if it is equal to the `target`. This process continues until all possible subarrays have been checked.

Finally, the function returns the `max_sum`, which is the maximum sum of any contiguous subarray in the `numbers` list that is equal to the `target` sum.

To use the function, you can call it with the `numbers` list `[-2, -3, 4, -1,