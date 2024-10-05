The `FindZero` function uses the bisection method to find a root of the polynomial. The bisection method is a root-finding method that repeatedly bisects an interval and then selects a subinterval in which a root must lie for further processing.

Here is the step-by-step explanation of the `FindZero` function:

1. Define the maximum number of iterations (in this case, 100).
2. Initialize the interval [a, b] with a large value for a and a small value for b. These values will be adjusted as the algorithm progresses.
3. For each iteration:
   - Compute the midpoint of the interval (c = (a + b) / 2).
   - Evaluate the polynomial at the midpoint (f(c)).
   - If f(c) is close to zero (within a small tolerance), return c as the root.
   - If f(c) is positive, update the interval [a, b] to [a, c].
   - If f(c) is negative, update the interval [a, b] to [c, b].
4. If the algorithm reaches the maximum number of iterations without finding a root, return an error.

The `FindZero` function assumes that the polynomial has an even number of coefficients and that the largest non-zero coefficient is positive. This is because the bisection method requires that the polynomial changes sign across the root.

Here is the `FindZero` function in Go:

```go
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
func FindZero(xs []int) (float64, error) {
	const maxIterations = 100
	const tolerance = 1e-6

	a := math.MaxFloat64
	b := -math.MaxFloat