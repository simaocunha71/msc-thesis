Here's one way you could write the function:

```python
def odd_length_sum(nums):
    sum_odd_length = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            if (j-i) % 2 == 1:
                sum_odd_length += sum(nums[i:j])
    return sum_odd_length
```

Explanation:

The function `odd_length_sum` takes in an array of integers called `nums`. It initializes a variable `sum_odd_length` to 0, which will be the sum of all odd length subarrays. 

The function then uses two nested loops to iterate over all possible subarrays of `nums`. The outer loop iterates from 0 to the length of `nums`, and the inner loop iterates from the current index of the outer loop to the length of `nums` plus 1. 

Within the inner loop, the function checks if the length of the subarray (i.e., `j-i`) is odd by using the modulo operator `%`. If the length is odd, the function calculates the sum of the subarray by using slicing (`sum(nums[i:j])`) and adds it to `sum_odd_length`. 

After all subarrays have been checked, the function returns the final value of `sum_odd_length`. 

For example, if the input is `[1, 2, 4]`, the function will calculate the sum of the subarrays `[1]`, `[1, 2]`, `[2]`, `[1, 2, 4]`, and `[1, 4]`, which are all odd length subarrays. The sum of these subarrays is `1 + 3 + 2 + 10 = 16`, so the function will return 16.

The assertion `assert odd_length_sum([1,2,4]) == 14` checks if the function correctly calculates the sum of odd length subarrays for the input `[1, 2, 4]`, which should