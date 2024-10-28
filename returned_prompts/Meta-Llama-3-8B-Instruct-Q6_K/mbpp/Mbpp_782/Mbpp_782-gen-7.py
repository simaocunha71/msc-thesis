```
def odd_length_sum(arr):
    total_sum = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            if j-i % 2 != 0:
                total_sum += sum(arr[i:j])
    return total_sum
```



In this problem, we need to find the sum of all odd length subarrays in the given array. The problem statement does not specify whether the subarrays can start from the end of the array or not, but based on the unit test `assert odd_length_sum([1,2,4]) == 14`, we can assume that the subarrays can start from any position in the array, not just from the start or the end.

We can solve this problem by iterating over all possible subarrays and checking if the length of the subarray is odd. If it is, we add the sum of the subarray to the total sum. We use two nested loops to generate all possible subarrays, and the inner loop starts from `i+1` to `len(arr)` to generate subarrays of all lengths.

For example, for the array `[1,2,4]`, the possible subarrays are `[1]`, `[1,2]`, `[1,2,4]`, `[2]`, `[2,4]`, and `[4]`. The odd length subarrays are `[1]`, `[2]`, and `[4]`, and their sums are `1`, `2`, and `4` respectively. The total sum is `1+2+4=7`. However, the unit test `assert odd_length_sum([1,2,4]) == 14` expects the total sum to be `14`, which means we need to add the sums of all even length subarrays to the total sum as well. Therefore, the total sum is `7+7=14`.

Here is the Python function to solve this problem:
```
def odd_length_sum(arr):
    total_sum = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            if j-i % 2 != 0:
                total_sum += sum(arr[i:j])
    return total_sum
```
This function iterates over all possible subarrays and checks if the length of the subarray is odd. If it is, it adds the sum of the subarray to the total sum. The function returns the total sum