```go
// Evaluates polynomial with coefficients xs at point x.
// return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
func Poly(xs []int, x float64) float64{
    sum := 0.0
    for i, coeff := range xs {
        sum += float64(coeff) * math.Pow(x,float64(i))
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
    if len(xs)%2 != 0 {
        panic("Number of coefficients must be even")
    }
    maxCoeff := 0
    for _, coeff := range xs {
        if coeff > maxCoeff {
            maxCoeff = coeff
        }
    }
    if maxCoeff == 0 {
        panic("Largest non-zero coefficient must be non-zero")
    }
    x := -float64(xs[0])/float64(maxCoeff)
    return x
}
```
