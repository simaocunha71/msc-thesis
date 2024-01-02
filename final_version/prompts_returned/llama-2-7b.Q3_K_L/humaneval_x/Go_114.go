import (
    "math"
)

// Given an array of integers nums, find the minimum sum of any non-empty sub-array
// of nums.
// Example
// Minsubarraysum([2, 3, 4, 1, 2, 4]) == 1
// Minsubarraysum([-1, -2, -3]) == -6
func Minsubarraysum(nums []int) int {
    var result int
    if len(nums) < 2 {
        return math.MaxInt32
    }
    for i := 0; i + 1 < len(nums); i++ {
        s := sum(nums[i :])
        if s > result {
            result = s
        }
    }
    return result
}

func sum(slice []int) int {
    var ret int
    for _, v := range slice {
        ret += v
    }
    return ret
}