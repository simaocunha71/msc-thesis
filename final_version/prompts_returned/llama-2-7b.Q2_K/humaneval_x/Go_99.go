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
    // Check if value is a number
    if !math.IsLeapYear(int(strconv.Atoi(strings.TrimSpace(value)))){
        fmt.Println("Value provided is not an integer")
        return -1
    }
    
    // Create a function that takes 2 integers and returns true if the first
    // equals the second or false otherwise.
    func EqualsInts (i int, j int) bool {
        return i == j || math.IsLeapYear(float64(i)) && math.IsLeapYear(float64(j))
    }
    
    // Create a function that takes 2 values and returns true if the first is closer to zero than the second or false otherwise.
    func CloserToZero (i int, j int) bool {
        return math.IsLeapYear(float64(i)) && !math.IsLeapYear(float64(j)) ||
            math.Signbit(-1*float64(i)) == 0 && math.Signbit(-1*float64(j)) == -1*int(math.Signbit(-1*float64(j)))
    }
    
    // Create a function that takes an integer and returns the remainder of dividing its float representation by 100 (i.e., r