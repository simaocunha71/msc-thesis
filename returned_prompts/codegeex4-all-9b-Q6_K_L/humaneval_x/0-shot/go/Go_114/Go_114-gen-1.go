The problem can be solved using Kadane's algorithm, which is a dynamic programming approach used to solve problems involving maximum or minimum subarrays.

In this case, we want to find the minimum subarray sum. We can modify Kadane's algorithm to keep track of the minimum subarray sum instead of the maximum.

Here's the implementation:

```go
import (
    "math"
)

func Minsubarraysum(nums []int) int {
    if len(nums) == 0 {
        return 0
    }

    minSum := math.MaxInt32
    currentSum := 0

    for _, num := range nums {
        currentSum = min(num, currentSum+num)
        minSum = min(minSum, currentSum)
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

Let's break down the code:

1. We first check if the input array is empty. If it is, we return 0 as the minimum subarray sum.
2. We initialize `minSum` to `math.MaxInt32` and `currentSum` to 0. `minSum` will hold the minimum subarray sum, and `currentSum` will hold the current subarray sum.
3. We iterate through each number in the input array.
4. For each number, we update `currentSum` to be the minimum of the current number and the sum of the current number and `currentSum`. This ensures that we always have the smallest subarray sum so far.
5. We update `minSum` to be the minimum of `minSum` and `currentSum`.
6. Finally, we return `minSum` as the result.

This algorithm runs in O(n) time complexity, where n is the length of the input array.