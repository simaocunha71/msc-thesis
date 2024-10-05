Here is the solution for the problem. The `FindZero` function calculates the root of a polynomial using the Newton's method. It iteratively updates the estimate of the root until the error is small enough. The initial estimate is set to 0. The `Poly` function is used to calculate the polynomial value at a given point.

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
// FindZero returns only one zero point, even if there are many.
// Moreover, FindZero only takes list xs having even number of coefficients
// and largest non zero coefficient as it guarantees
// a solution.
func FindZero(xs []int) float64 {
    if len(xs)%2 != 0 || xs[0] == 0 {
        panic("xs must have even number of coefficients and largest non zero coefficient")
    }
    x := 0.0
    for {
        y := Poly(xs, x)
        if math.Abs(y) < 1e-6 {
            return x
        }
        x -= y / Poly(xs[:len(xs)-1], x)
    }
}
```

This code will work for any polynomial with even number of coefficients and largest non zero coefficient. It uses Newton's method to find the root of the polynomial. The initial estimate of the root is set to 0, and it iteratively updates the estimate until the error is small enough. The error is considered small enough when the absolute value of the polynomial value at the current estimate is less than 1e-6. The final estimate is returned as the root of the polynomial. If the polynomial does not have a root, the function will run indefinitely. In this case, you can add a maximum number of iterations and return the last estimate if the error is still large after the maximum number of iterations. 

Please note that this code does not guarantee to find all roots of a polynomial. It only finds one root. If you need to find all roots, you need to use a