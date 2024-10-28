    result := math.MaxInt32
    currSum := 0

    for i := 0; i < len(nums); i++ {
        currSum = 0
        for j := i; j < len(nums); j++ {
            currSum += nums[j]
            result = min(result, currSum)
        }
    }

    return result
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

// Time: O(n^2)
// Space: O(1)




*/

import (
    "math"
)

// Given an array of integers nums, find the minimum sum of any non-empty sub-array
// of nums.
// Example
// Minsubarraysum([2, 3, 4, 1, 2, 4]) == 1
// Minsubarraysum([-1, -2, -3]) == -6
func Minsubarraysum(nums []int) int {

    result := math.MaxInt32
    currSum := 0

    for i := 0; i < len(nums); i++ {
        currSum = 0
        for j := i; j < len(nums); j++ {
            currSum += nums[j]
            result = min(result, currSum)
        }
    }

    return result
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

// Time: O(n^2)
// Space: O(1)




*/




func Minsubarraysum(nums []int) int {
    result := math.MaxInt32
    currSum := 0
    for i := 0; i < len(nums); i++ {
        currSum = 0
        for j := i; j < len(nums); j++ {
            currSum += nums[j]
            result = min(result, currSum)