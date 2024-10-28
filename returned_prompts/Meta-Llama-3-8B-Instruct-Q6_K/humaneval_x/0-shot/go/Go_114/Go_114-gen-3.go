```go
import (
    "math"
)

func Minsubarraysum(nums []int) int {
    minSum := math.MaxInt64
    sum := 0
    for _, num := range nums {
        sum += num
        minSum = min(minSum, sum)
        if sum < 0 {
            sum = 0
        }
    }
    return minSum
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```
Explanation:
The problem is asking to find the minimum sum of any non-empty sub-array of the given array. This can be solved by iterating over the array and maintaining a running sum. If the sum becomes negative, it means the current sub-array is not contributing to the minimum sum, so we reset the sum to 0.

We also keep track of the minimum sum seen so far. The minimum sum can be updated whenever we see a smaller sum. At the end of the iteration, the minimum sum will be the minimum sum of any non-empty sub-array.

The time complexity of this solution is O(n), where n is the length of the input array, because we are iterating over the array once. The space complexity is O(1), because we are using a constant amount of space to store the sum and the minimum sum.