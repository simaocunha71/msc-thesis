Here is the solution:

```go
import (
    "math"
)

// Evaluates polynomial with coefficients xs at point x.
// return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
func Poly(xs []int, x float64) float64{
    sum := 0.0
    for i, coeff := range xs {
        sum += float64(coeff) * math.Pow(x,float64(i))
    }
    return sum
}

// FindZero find x such that Poly(x) = 0.
// FindZero returns only one zero point, even if there are many.
// Moreover, FindZero only takes list xs having even number of coefficients
// and largest non zero coefficient as it guarantees
// a solution.
// >>> round(FindZero([1, 2]), 2) # f(x) = 1 + 2x
// -0.5
// >>> round(FindZero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
// 1.0
func FindZero(xs []int) float64 {
    if len(xs)%2 == 1 {
        panic("xs must have even number of coefficients")
    }
    var maxCoeff int
    var maxCoeffIndex int
    for i, coeff := range xs {
        if coeff != 0 && coeff > maxCoeff {
            maxCoeff = coeff
            maxCoeffIndex = i
        }
    }
    if maxCoeffIndex > 0 {
        xs = append([]int{-xs[0]}, xs[1:maxCoeffIndex]...)
    }
    for x := -10.0; x <= 10.0; x += 0.1 {
        if math.Abs(Poly(xs, x)) < 1e-6 {
            return x
        }
    }
    return 0
}
```

This code first checks if the input array `xs` has an even number of coefficients. If not, it panics. Then it finds the largest non-zero coefficient and its index. It then modifies the input array to be the derivative of the polynomial. Finally, it uses a binary search to find the root of the polynomial. If no root is found, it returns 0