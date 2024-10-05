import (
    "math"
)

// Given a positive integer n, return the count of the numbers of n-digit
// positive integers that start or end with 1.
func StartsOneEnds(n int) int {
    if n == 1 {
        return 10
    }
    count := 0
    for i := 1; i <= 9; i++ {
        count += int(math.Pow(10, n-2) * math.Pow(9, n-2))
    }
    return count
}
