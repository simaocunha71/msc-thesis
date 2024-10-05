The problem is asking for the minimum sum of any non-empty sub-array of the given array. This can be achieved by using a sliding window approach with a priority queue. Here is the solution in Go:
```go
import (
    "math"
)

func Minsubarraysum(nums []int) int {
    minSum := math.MaxInt64
    windowSum := 0
    windowStart := 0

    for windowEnd := 0; windowEnd < len(nums); windowEnd++ {
        windowSum += nums[windowEnd]

        for windowSum > minSum {
            windowSum -= nums[windowStart]
            windowStart++
        }

        minSum = math.Min(minSum, windowSum)
    }

    return minSum
}
```
Here's an explanation of the solution:

1. We initialize the minimum sum to a large value (`math.MaxInt64`) and the window sum to 0.
2. We iterate through the array with a sliding window approach, updating the window sum and window start index.
3. If the window sum exceeds the minimum sum, we subtract the first element of the window from the window sum and increment the window start index.
4. We update the minimum sum with the current window sum if it is smaller.
5. Finally, we return the minimum sum.

This solution has a time complexity of O(n), where n is the length of the input array, and a space complexity of O(1) since we only use a few extra variables.