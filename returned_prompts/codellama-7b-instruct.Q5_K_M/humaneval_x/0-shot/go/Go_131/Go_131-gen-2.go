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
    for n > 0 {
        lastDigit := n % 10
        if lastDigit % 2 == 1 {
            result *= lastDigit
        }
        n /= 10
    }
    return result
}
