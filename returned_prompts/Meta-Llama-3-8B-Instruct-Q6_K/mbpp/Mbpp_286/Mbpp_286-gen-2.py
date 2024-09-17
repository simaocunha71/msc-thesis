```
def max_sub_array_sum_repeated(arr, k, n):
    total_sum = sum(arr) * k
    max_sum = float('-inf')
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub_sum = sum(arr[i:j])
            max_sum = max(max_sum, sub_sum)
    return max_sum
```


The problem is asking to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times. The input array is `arr`, the number of times it should be repeated is `k`, and the total length of the modified array is `n`.

The unit test `assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30` suggests that the array should be repeated 4 times and the total length of the modified array is 12.

The solution uses two loops to find all the possible contiguous arrays in the modified array. The `total_sum` variable is used to store the sum of the array repeated k times. The `max_sum` variable is used to store the maximum sum of a contiguous array found so far. The function returns the maximum sum.

The time complexity of this solution is O(n^2) because of the two nested loops. The space complexity is O(1) because it only uses a constant amount of space. 

Please note that this solution is not efficient for large inputs. A more efficient solution would be to use a sliding window approach with a time complexity of O(n). 

Here is a more efficient solution:

```
def max_sub_array_sum_repeated(arr, k, n):
    total_sum = sum(arr) * k
    max_sum = float('-inf')
    current_sum = 0
    for i in range(n):
        current_sum += arr[i % len(arr)]
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum
```

This solution uses a sliding window approach to find the maximum sum of a contiguous array. It keeps track of the current sum of the array and updates the maximum sum if the current sum is greater. If the current sum becomes negative, it resets the current sum to 0. The time complexity of this solution is O(n) and the space complexity is O(1). 