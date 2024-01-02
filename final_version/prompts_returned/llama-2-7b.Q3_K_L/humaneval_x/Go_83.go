import (
    "math"
)

// Given a positive integer n, return the count of the numbers of n-digit
// positive integers that start or end with 1.
func StartsOneEnds(n int) int {
	if n < 2 || n > 9 {
		return 0
	} else if n == 2 {
		return 4
	} else if n % 3 == 0 && n % 5 != 0 {
		return 2
	} else if n % 7 == 0 {
		return 1
	} else if n % (9 + 1) < 2 || n % (9 - 1) > 6 {
		return 0
	} else {
		if n%3 == 2 {
			return 2
		} else if n%5 == 4 {
			return 1
		} else if n % (9 + 1) < 2 || n % (9 - 1) > 6 {
			return 0
		}
	}
	return 0
}

// Given a positive integer n, return the count of the numbers of n-digit
// positive integers that consist only in 1s.
func EndsOne(n int) int {
	if n < 2 || n > 9 {
		return 0
	} else if n % (10 - 1) == 0 {
		return 1
	}
	return 0
}
