```go
package main

import (
	"fmt"
	"math"
)

// Evaluates polynomial with coefficients xs at point x.
// return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
func Poly(xs []int, x float64) float64 {
	sum := 0.0
	for i, coeff := range xs {
		sum += float64(coeff) * math.Pow(x, float64(i))
	}
	return sum
}

// xs are coefficients of a polynomial.
// FindZero find x such that Poly(x) = 0.
// FindZero returns only only zero point, even if there are many.
// Moreover, FindZero only takes list xs having even number of coefficients
// and largest non zero coefficient as it guarantees
// a solution.
// >>> round(FindZero([1, 2]), 2) # f(x) = 1 + 2x
// -0.5
// >>> round(FindZero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
// 1.0
func FindZero(xs []int) float64 {
	// Check if the number of coefficients is even
	if len(xs)%2 != 0 {
		panic("Number of coefficients must be even")
	}

	// Find the largest non-zero coefficient
	var maxCoeff int
	for _, coeff := range xs {
		if coeff != 0 && abs(coeff) > abs(maxCoeff) {
			maxCoeff = coeff
		}
	}

	// Define the range for searching the zero
	start := float64(-maxCoeff)
	end := float64(maxCoeff)

	// Use binary search to find the zero
	for start < end {
		mid := (start + end) / 2
		polyVal := Poly(xs, mid)
		if polyVal == 0 {
			return mid
		} else if polyVal < 0 {
			start = mid
		} else {
			end = mid
		}
	}

	// Return the found zero
	return (start + end) / 2
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main