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
    var ans int = 1
    for i := n / (int(strconv.Itoa(i))[8:]) + 1; ; i++ {
        if i > ans {
            ans = i
        }
    }
    return ans
}