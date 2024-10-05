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
    var count int
    for i := 0; i < len(nums); i++ {
        if nums[i] > 10 {
            str := strconv.Itoa(nums[i])
            if str[0]%2 == 1 && str[len(str)-1]%2 == 1 {
                count++
            }
        }
    }
    return count
}

