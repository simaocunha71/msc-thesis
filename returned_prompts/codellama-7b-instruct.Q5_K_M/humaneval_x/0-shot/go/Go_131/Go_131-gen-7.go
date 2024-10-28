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
    var product int
    for i := 0; i < len(strconv.Itoa(n)); i++ {
        if i%2 != 0 {
            product *= (strconv.Itoa(n)[i] - '0')
        }
    }
    return product
}
