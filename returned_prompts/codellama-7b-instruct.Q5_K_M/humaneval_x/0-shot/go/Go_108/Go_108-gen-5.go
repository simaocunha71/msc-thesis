import (
    "math"
    "strconv"
)

// Write a function CountNums which takes an array of integers and returns
// the number of elements which has a sum of digits > 0.
// If a number is negative, then its first signed digit will be negative:
// e.g. -123 has signed digits -1, 2, and 3.
// >>> CountNums([]) == 0
// >>> CountNums([-1, 11, -11]) == 1
// >>> CountNums([1, 1, 2]) == 3
func CountNums(arr []int) int {
    var count int
    for _, i := range arr {
        var sum int
        for _, j := range strconv.Itoa(i) {
            sum += int(j - '0')
        }
        if sum > 0 {
            count++
        }
    }
    return count
}


