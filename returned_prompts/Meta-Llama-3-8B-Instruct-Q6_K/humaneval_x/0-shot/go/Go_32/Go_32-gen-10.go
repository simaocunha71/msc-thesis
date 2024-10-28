Here is a simple solution using Newton's method to find the root of the polynomial. The Newton's method is an iterative method that starts with an initial guess and refines it until it converges to the root.

```go
import (
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
    if len(xs)%2 != 0 {
        panic("xs must have even number of coefficients")
    }
    if xs[0] == 0 {
        return 0
    }
    maxCoeffIndex := 0
    for i := 1; i < len(xs); i++ {
        if math.Abs(float64(xs[i])) > math.Abs(float64(xs[maxCoeffIndex])) {
            maxCoeffIndex = i
        }
    }
    x := float64(maxCoeffIndex)
    for {
        fx := Poly(xs, x)
        if math.Abs(fx) < 1e-6 {
            return x
        }
        dx := Poly(xs, x+1)-Poly(xs, x-1)
        if dx == 0 {
            dx = 1e-6
        }
        x -= fx / dx
    }
}
```

This solution works by initializing the guess for the root to the index of the maximum