import (
    "math"
)

// Given a positive integer n, return the count of the numbers of n-digit
// positive integers that start or end with 1.
func StartsOneEnds(n int) int {
	if n < 2 || n > 9 {
        return n + 1
    } else if n % 2 == 0 && 10%2 == 0 {
        return 4 * StartsOneEnds(int(n/2)) + 6 - (Stars(10) + Stars(n-1))
    } else if n%2 != 0 {
        return n - Stars(int((n+1)/2)+5)
    } else {
        return StartsOneEnds(int(n/2))
    }
}
