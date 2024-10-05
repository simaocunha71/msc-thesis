	binary := ""
	for decimal > 0 {
		if decimal%2 == 0 {
			binary = "0" + binary
		} else {
			binary = "1" + binary
		}
		decimal = decimal / 2
	}
	return "db" + binary + "db"
}

func main() {
	fmt.Println(DecimalToBinary(15))
	fmt.Println(DecimalToBinary(32))
}
```

The code above converts a decimal number to binary using the algorithm that repeatedly divides the number by 2 and appends the remainder to the binary string. It then adds "db" at the beginning and at the end of the binary string to meet the requirements of the problem.

## Problem 2:

Given an array of integers, find the maximum sum of any contiguous subarray of the array. The array can contain both positive and negative numbers.

For example, if the array is [-2, 1, -3, 4, -1, 2, 1, -5, 4], the maximum sum would be 6 (4, -1, 2, 1).

### Solution:

This problem can be solved using Kadane's algorithm. It has a time complexity of O(n).

Here is the Go code for the problem:

```go
package main

import (
	"fmt"
	"math"
)

// Function to find the maximum sum of contiguous subarray
func maxSubArray(nums []int) int {
	maxSoFar := nums[0]
	maxEndingHere := nums[0]

	for i := 1; i < len(nums); i++ {
		maxEndingHere = int(math.Max(float64(nums[i]), float64(maxEndingHere+nums[i])))
		maxSoFar = int(math.Max(float64(maxSoFar), float64(maxEndingHere)))
	}

	return maxSoFar
}

func main() {
	nums := []int{-2, 1, -3, 4, -