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
    for _, num := range nums {
        if num > 10 {
            str := strconv.Itoa(num)
            if str[0] == "1" || str[0] == "3" || str[0] == "5" || str[0] == "7" || str[0] == "9" {
                if str[len(str)-1] == "1" || str[len(str)-1] == "3" || str[len(str)-1] == "5" || str[len(str)-1] == "7" || str[len(str)-1] == "9" {
                    count++
                }
            }
        }
    }
    return count
}