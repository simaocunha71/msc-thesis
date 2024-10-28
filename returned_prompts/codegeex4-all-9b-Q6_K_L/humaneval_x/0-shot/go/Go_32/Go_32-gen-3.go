The function `FindZero` is intended to find a zero of a polynomial given its coefficients. However, the current implementation of `FindZero` does not actually find a zero of the polynomial; instead, it simply returns the value of the polynomial evaluated at `-1.0`. This is because there is no loop to iterate over the polynomial and calculate its value at different points, which is necessary to find a zero.

Here's a corrected version of the `FindZero` function that uses the `Poly` function to evaluate the polynomial at different points and find a zero:

```go
func FindZero(xs []int) float64 {
    // Start with an initial guess for the zero
    x := -1.0

    // Iterate until we find a zero
    for {
        // Evaluate the polynomial at the current guess
        f := Poly(xs, x)

        // Check if the polynomial is close to zero
        if math.Abs(f) < 1e-6 {
            // If the polynomial is close to zero, we've found a zero
            return x
        }

        // Update the guess for the zero
        x += 0.1
    }
}
```

This corrected version of `FindZero` uses a simple iterative approach to find a zero of the polynomial. It starts with an initial guess of `-1.0` and then iteratively updates the guess by adding `0.1` until the polynomial is close to zero (within a tolerance of `1e-6`). Once the polynomial is close to zero, the function returns the current guess as the zero of the polynomial.

Note that this is a simple and not very efficient method for finding a zero of a polynomial. In practice, more sophisticated methods such as the Newton-Raphson method or the bisection method would be used.