```go
import (
	"fmt"
	"sort"
	"strconv"
)

// Write a function which sorts the given list of integers
// in ascending order according to the sum of their digits.
// Note: if there are several items with similar sum of their digits,
// order them based on their index in original list.
// 
// For example:
// >>> OrderByPoints([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
// >>> OrderByPoints([]) == []
func OrderByPoints(nums []int) []int {
	// Sort the nums slice in ascending order based on the sum of their digits
	sort.Slice(nums, func(i, j int) bool {
		sumI := sumDigits(nums[i])
		sumJ := sumDigits(nums[j])

		// If the sums are equal, order by their original indexes
		if sumI == sumJ {
			return i < j
		}

		// Otherwise, order by the sum of their digits
		return sumI < sumJ
	})

	return nums
}

func sumDigits(n int) int {
	// Convert the number to a string to iterate over its digits
	str := strconv.Itoa