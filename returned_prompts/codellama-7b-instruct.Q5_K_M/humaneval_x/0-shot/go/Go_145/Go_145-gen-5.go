import (
    "sort"
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
        return sumDigits(nums[i]) < sumDigits(nums[j])
    })
    return nums
}

func sumDigits(n int) int {
    var sum int
    for n > 0 {
        sum += n % 10
        n /= 10
    }
    return sum
}

// B:
import (
    "sort"
    "strconv"
)

//