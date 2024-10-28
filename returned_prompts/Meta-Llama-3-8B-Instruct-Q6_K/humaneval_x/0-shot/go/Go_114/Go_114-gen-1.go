The problem is asking to find the minimum sum of any non-empty sub-array of the given array of integers. 

Here's a Python solution for this problem:

```Python
def minSubArraySum(nums):
    if not nums:
        return 0

    min_sum = float('inf')
    current_sum = 0

    for num in nums:
        current_sum += num
        min_sum = min(min_sum, current_sum)
        if current_sum > 0:
            current_sum = 0

    return min_sum
```

The idea is to keep a running sum of the sub-array and update the minimum sum whenever we find a smaller sum. If the running sum becomes positive, we reset it to 0 to start a new sub-array. This way, we ensure that we consider all non-empty sub-arrays and find the minimum sum among them.

In the given example, the function Minsubarraysum([2, 3, 4, 1, 2, 4]) returns 1, which is the minimum sum of any non-empty sub-array in the given array. Similarly, Minsubarraysum([-1, -2, -3]) returns -6, which is the minimum sum of any non-empty sub-array in the given array. 

The function Minsubarraysum is defined as follows:

```go
func Minsubarraysum(nums []int) int {
    if len(nums) == 0 {
        return 0
    }

    min_sum := math.MaxInt64
    current_sum := 0

    for _, num := range nums {
        current_sum += num
        if current_sum < min_sum {
            min_sum = current_sum
        }
        if current_sum > 0 {
            current_sum = 0
        }
    }

    return min_sum
}
``` 

This Go function works similarly to the Python function. It initializes the minimum sum to the maximum possible integer value and the current sum to 0. It then iterates over the array, adding each number to the current sum and updating the minimum sum if necessary. If the current sum becomes positive, it resets the current sum to 0 to start a new sub-array. Finally, it returns the minimum sum. 

The function Minsubarraysum([2, 3, 4, 1, 2, 4]) returns 1, and Minsubarraysum([-1, -2, -3]) returns -6