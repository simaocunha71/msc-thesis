To solve the problem of finding the minimum sum of any non-empty sub-array from an array of integers, we can use a sliding window approach. This method is efficient and suitable for this type of problem, where we need to find the minimum sum of sub-arrays with varying lengths.

Here is the complete code:

```go
package main

import (
	"fmt"
	"math"
)

// Minsubarraysum calculates the minimum sum of any non-empty sub-array of nums.
func Minsubarraysum(nums []int) int {
	if len(nums) == 0 {
		return 0 // Edge case: if the input array is empty, return 0.
	}

	// Initialize the minimum sum as the maximum possible integer value.
	minSum := math.MaxInt32

	// Initialize the current sum with the first element.
	currentSum := nums[0]

	// Update the minimum sum if the first element is smaller.
	if currentSum < minSum {
		minSum = currentSum
	}

	// Iterate through the array starting from the second element.
	for i := 1; i < len(nums); i++ {
		// Update the current sum by either adding the current element
		// or considering a new sub-array starting from the current element.
		currentSum = int(math.Min(float64(currentSum+nums[i]), float64(nums[i])))

		// Update the minimum sum if the current sum is smaller.
		if currentSum < minSum {
			minSum = currentSum
		}
	}

	return minSum
}

func main() {
	// Test cases
	fmt.Println(Minsubarraysum([]int{2, 3, 4, 1, 2, 4})) // Output: 1
	fmt.Println(Minsubarraysum([]int{-1, -2, -3}))      // Output: -6
}
```

### Explanation:
1. **Initialization**: We start by checking if the input array is empty. If it is, we return 0 as there are no sub-arrays to consider.
2. **Sliding Window**: We iterate through the array starting from the second element. For each element, we decide whether to add it to the current sum or start a new sub-array with the current element as its first element. This decision is based on which option gives a smaller sum.
3. **Updating Minimum Sum**: We keep track of the minimum sum encountered so far and update it whenever we find a smaller