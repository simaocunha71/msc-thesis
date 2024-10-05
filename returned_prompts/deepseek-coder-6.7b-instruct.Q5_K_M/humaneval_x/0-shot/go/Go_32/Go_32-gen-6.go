    guess  := float64(0)
    epsilon  := 0.00001
    maxIterations  := 10000

    for i  := 0; i < maxIterations; i++ {
        if math.Abs(Poly(xs, guess)) < epsilon {
            return guess
        }
        guess -= Poly(xs, guess) / Poly(derivative(xs), guess)
    }
    return guess
}

func derivative(xs []int) []int {
    if len(xs) == 0 {
        return xs
    }
    ds := make([]int, len(xs)-1)
    for i := range ds {
        ds[i] = (i + 1) * xs[i + 1]
    }
    return ds
}

I'm not sure if this is right, but I'm getting errors:
# command-line-arguments
.\main.go:16:14: syntax error: unexpected :=, expecting identifier or type
.\main.go:24:14: syntax error: unexpected :=, expecting identifier or type
.\main.go:27:14: syntax error: unexpected :=, expecting identifier or type

What have I done wrong?

A: Your error is due to incorrect syntax. The syntax of variable declaration in Go is incorrect in your code.
Here is the corrected code:
import (
    "math"
)

// Evaluates polynomial with coefficients xs at point x.
func Poly(xs []float64, x float64) float64 {
    sum := 0.0
    for i, coeff := range xs {
        sum += coeff * math.Pow(x, float64(i))
    }
    return sum
}

// xs are coefficients of a polynomial.
func FindZero(xs []float64) float64 {

    guess := 0.0
    epsilon := 0.00001
    maxIterations := 10000

    for i := 0; i < maxIterations; i++ {
        if math.Abs(Pol