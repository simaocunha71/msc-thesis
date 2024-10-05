To solve this problem, you need to implement a numerical method for finding the roots of a polynomial. One of the simplest methods for this purpose is the Newton-Raphson method, also known as the Newton method.

The Newton-Raphson method is an iterative algorithm that is used to find successively better approximations to the roots (or zeroes) of a real-valued function.

Here is the implementation of the Newton-Raphson method in Go:

```go
import (
	"math"
)

// Evaluates polynomial with coefficients xs at point x.
func Poly(xs []int, x float64) float64 {
	sum := 0.0
	for i, coeff := range xs {
		sum += float64(coeff) * math.Pow(x, float64(i))
	}
	return sum
}

// Computes the derivative of the polynomial at the given point.
func PolyDerivative(xs []int, x float64) float64 {
	sum := 0.0
	for i, coeff := range xs {
		if i > 0 {
			sum += float64(i) * float64(coeff) * math.Pow(x, float64(i-1))
		}
	}
	return sum
}

// FindZero finds a root of the polynomial.
func FindZero(xs []int) float64 {
	// Initial guess
	x := 0.0

	// Tolerance for stopping the iteration
	tolerance := 1e-6

	// Maximum number of iterations
	maxIterations := 1000

	for i := 0; i < maxIterations; i++ {
		f := Poly(xs, x)
		fPrime := PolyDerivative(xs, x)
		if math.Abs(fPrime) < tolerance {
			// The derivative is too small, we cannot continue.
			return math.NaN()
		}
		x = x - f/fPrime
		if math.Abs(f) < tolerance {
			// We have found a root.
			return x
		}
	}
	// We did not find a root.
	return math.NaN()
}
```

This function will return NaN if it cannot find a root. Also, this function assumes that the input polynomial has an even number of coefficients and the largest non-zero coefficient is positive. If these conditions are not met, the function may not work correctly.

Please note that this is a simple implementation of the Newton-Raphson method and it may not be the best choice for all cases. For example, it does not handle the case where the polynomial has