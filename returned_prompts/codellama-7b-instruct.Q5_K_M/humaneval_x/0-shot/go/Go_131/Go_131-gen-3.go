import (
    "strconv"
)

// Given a positive integer n, return the product of the odd Digits.
// Return 0 if all Digits are even.
// For example:
// Digits(1)  == 1
// Digits(4)  == 0
// Digits(235) == 15
func Digits(n int) int {

    var result int
    var num string
    num = strconv.Itoa(n)
    for i := 0; i < len(num); i++ {
        if num[i]%2 == 0 {
            result = result * int(num[i] - 48)
        }
    }
    return result
}
