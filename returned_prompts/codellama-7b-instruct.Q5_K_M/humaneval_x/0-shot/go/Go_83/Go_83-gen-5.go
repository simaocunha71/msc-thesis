import (
    "math"
)

// Given a positive integer n, return the count of the numbers of n-digit
// positive integers that start or end with 1.
func StartsOneEnds(n int) int {
    // 1. Check for n < 1.
    if n < 1 {
        return 0
    }

    // 2. Calculate the number of digits in the result.
    count := 0
    for i := 1; i <= n; i++ {
        count += math.Pow(10, i-1)
    }

    // 3. Calculate the number of digits that start with 1.
    ones := 0
    for i := 1; i < n; i++ {
        ones += math.Pow(10, i)
    }

    // 4. Calculate the number of digits that end with 1.
    ones += math.Pow(10, n-1)

    // 5. Return the count of the numbers that start or end with 1.
    return count - ones
}

