To find a zero of a polynomial, we can use Newton’s method. Starting with an initial guess, we repeatedly apply Newton’s method to refine the approximation. Here’s how Newton’s method works:

1. Evaluate the function at the current approximation.
2. Compute the derivative of the function at the current approximation.
3. Subtract the result of step 1 divided by the result of step 2 to obtain the next approximation.

Here’s Go code to implement Newton’s method to find a zero of a polynomial:

```go
package main

import (
    "fmt"
    "math"
)

func poly(xs []int, x float64) float64 {
    sum := 0.0
    for i, coeff := range xs {
        sum += math.Pow(x, float64(i)) * float64(coeff)
    }
    return sum
}

func derivative(xs []int, x float64) float64 {
    sum := 0.0
    for i, coeff := range xs {
        sum += math.Pow(x, float64(i)) * float64(coeff) * float64(i)
    }
    return sum
}

func findZero(xs []int) float64 {
    x := 1.0
    for {
        if poly(xs, x) < 1e-8 {
            return x
        }
        if derivative(xs, x) < 0 {
            x /= 2
        } else {
            x *= 2
        }
    }
}

func main() {
    fmt.Println(findZero([]int{1, 2}))
    fmt.Println(findZero([]int{-6, 11, -6, 1}))
}
```

The code defines two functions: poly and derivative. The poly function evaluates the polynomial at a given point. The derivative function computes the derivative of the polynomial at a given point. The findZero function implements Newton’s method to find a zero of a polynomial.

We start with an initial guess of 1.0. If the polynomial value is very small at the current