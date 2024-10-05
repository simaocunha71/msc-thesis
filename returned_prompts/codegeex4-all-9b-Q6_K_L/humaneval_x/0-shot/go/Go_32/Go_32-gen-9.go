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
func FindZero(xs []int) float64 {
	var x float64
	if len(xs)%2 == 0 {
		x = float64(xs[len(xs)-1])
	} else {
		x = float64(xs[len(xs)-1]) / 2
	}
	for i := 0; i < 10000; i++ {
		y := Poly(xs, x)
		if math.Abs(y) < 1e-9 {
			return x
		}
		x -= y / Poly(xs, x-1)
	}
	return x
}

func main() {
	// Example usage
	fmt.Println(FindZero([]int{1, 2}))          // f(x) = 1 + 2x
	fmt.Println(FindZero([]int{-6, 11, -6, 1})) // (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
}
```
