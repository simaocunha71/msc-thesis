The problem is asking for the minimum sum of any non-empty sub-array of a given array of integers. In other words, we need to find the smallest possible sum of a continuous part of the array.

Here is a possible solution in Go:

```go
import (
    "math"
)

func Minsubarraysum(nums []int) int {
    // Initialize the minimum sum as the maximum possible value
    minSum := math.MaxInt32

    // Iterate over the array
    for i := 0; i < len(nums); i++ {
        currentSum := 0

        // Calculate the sum of sub-arrays starting from index i
        for j := i; j < len(nums); j++ {
            currentSum += nums[j]

            // Update the minimum sum if the current sum is smaller
            if currentSum < minSum {
                minSum = currentSum
            }
        }
    }

    return minSum
}
```
This solution iterates over each possible sub-array and calculates its sum, updating the minimum sum if the current sum is smaller. The time complexity of this solution is O(n^2), where n is the length of the input array. This might not be the most efficient solution, but it should work for small input sizes. For larger input sizes, a more efficient algorithm would be needed.