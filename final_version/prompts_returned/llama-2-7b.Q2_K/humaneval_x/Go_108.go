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
    res := arr[0]
    for _, v := range arr[1:] {
        if intToStr(v+res)%10 > 0 { // check digit
            res += intToStr(v + res) % 10 // add digit to total
        } else { // no digit exceeds 0
        }
    }
    return res
}