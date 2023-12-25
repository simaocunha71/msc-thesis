import (
    "strconv"
)

// Write a function that takes an array of numbers as input and returns
// the number of elements in the array that are greater than 10 and both
// first and last digits of a number are odd (1, 3, 5, 7, 9).
// For example:
// Specialfilter([15, -73, 14, -15]) => 1
// Specialfilter([33, -2, -3, 45, 21, 109]) => 2
func Specialfilter(nums []int) int {
    var result = 0
    for _, num := range nums {
        if (((num>>1) & 1) == (num >> 1) && (num&1 != 0)) || ((num&-1) == (-num - 1)) {
            continue
        } else {
            return result + 1
        }
    }
}
