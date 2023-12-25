import (
    "math"
)

// Given an array of integers nums, find the minimum sum of any non-empty sub-array
// of nums.
// Example
// Minsubarraysum([2, 3, 4, 1, 2, 4]) == 1
// Minsubarraysum([-1, -2, -3]) == -6
func Minsubarraysum(nums []int) int {
    sum := math.MaxInt64
    for _, num := range nums {
        sum += num * (i+1) // i is subscript of nums from 0 to i-1
        if sum < minSum {
            minSum = sum
        }
    }
    return minSum
}
