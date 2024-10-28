import (
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
	sort.Slice(nums, func(i, j int) bool {
		sumI := sumDigits(nums[i])
		sumJ := sumDigits(nums[j])
		if sumI == sumJ {
			return i < j
		}
		return sumI < sumJ
	})
	return nums
}

func sumDigits(n int) int {
	sum := 0
	for _, c := range strconv.Itoa(n) {
		digit, _ := strconv.Atoi(string(c))
		sum += digit
	}
	return sum
}

