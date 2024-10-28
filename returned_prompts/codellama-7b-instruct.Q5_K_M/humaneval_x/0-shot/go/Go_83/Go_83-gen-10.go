import (
    "math"
)

// Given a positive integer n, return the count of the numbers of n-digit
// positive integers that start or end with 1.
func StartsOneEnds(n int) int {
    if n < 1 {
        return 0
    }
    if n == 1 {
        return 1
    }
    return int(math.Pow(10, n-1))
}
