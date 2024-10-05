    // the count of the numbers of n-digit positive integers that start or end with 1.
    count := 0

B:
    // calculate the count
    count = 2 * int(math.Pow(10, float64(n-1)))

C:
    return count
}

// Test the function with a few cases
func main() {
    fmt.Println(StartsOneEnds(1))  // should print 2
    fmt.Println(StartsOneEnds(2))  // should print 40
    fmt.Println(StartsOneEnds(3))  // should print 800
    fmt.Println(StartsOneEnds(4))  // should print 16000
}
*/

import (
	"math"
)

// Given a positive integer n, return the count of the numbers of n-digit
// positive integers that start or end with 1.
func StartsOneEnds(n int) int {
	count := 2 * int(math.Pow(10, float64(n-1)))
	return count
}

// Test the function with a few cases
func main() {
	fmt.Println(StartsOneEnds(1))  // should print 2
	fmt.Println(StartsOneEnds(2))  // should print 40
	fmt.Println(StartsOneEnds(3))  // should print 800
	fmt.Println(StartsOneEnds(4))  // should print 16000
}

/*
The function StartsOneEnds(n int) int takes in a positive integer n and calculates the count of the numbers of n-digit positive integers that start or end with 1. It does this by multiplying 2 by 10 to the power of (n-1). This is because for each n-digit number there are 2 numbers that start with 1 (one digit number and n-digit numbers), and for each of these there are 10 choices for the second digit (0-9). For the numbers that end with 1, there are also 10 choices for the last digit