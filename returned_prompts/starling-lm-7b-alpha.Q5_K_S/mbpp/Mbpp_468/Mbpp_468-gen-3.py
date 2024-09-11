```
def max_product(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    if len(nums) == 3:
        return max(nums[0] * nums[1] * nums[2], max(nums[0], nums[1]), max(nums[0], nums[2]))
    inc_prev = [nums[0]]
    inc_curr = [nums[1]]
    for i in range(2, len(nums)):
        if nums[i] > inc_prev[len(inc_prev) - 1]:
            inc_curr.append(nums[i])
        else:
            while inc_prev[len(inc_prev) - 1] > nums[i]:
                inc_prev.pop()
            inc_prev.append(nums[i])
            inc_curr.append(max(inc_prev[len(inc_prev) - 1], inc_curr[len(inc_curr) - 1]))
    return max(inc_curr)
```

This is a greedy algorithm that uses an increasing subsequence to find the maximum product of the array. The algorithm first checks if the length of the array is 0, 1, or 2, and returns the maximum value. If the length of the array is 3, it returns the maximum product of the three numbers, as well as the maximum of the first two numbers and the maximum of the first and third numbers.

For arrays with more than three numbers, the algorithm uses two lists, `inc_prev` and `inc_curr`, to keep track of the increasing subsequence. The algorithm starts by initializing `inc_prev` with the first number of the array and `inc_curr` with the second number. Then, for each subsequent number in the array, the algorithm checks if it is greater than the last number in `inc_prev`. If it is, the number is added to `inc_curr`. Otherwise, the algorithm removes the last number from