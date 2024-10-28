import (
    "math"
    "strconv"
    "strings"
)

// Create a function that takes a value (string) representing a number
// and returns the closest integer to it. If the number is equidistant
// from two integers, round it away from zero.
// 
// Examples
// >>> ClosestInteger("10")
// 10
// >>> ClosestInteger("15.3")
// 15
// 
// Note:
// Rounding away from zero means that if the given number is equidistant
// from two integers, the one you should return is the one that is the
// farthest from zero. For example ClosestInteger("14.5") should
// return 15 and ClosestInteger("-14.5") should return -15.
func ClosestInteger(value string) int {
    // your code here
    intValue, _ := strconv.Atoi(value)
    return intValue
}
