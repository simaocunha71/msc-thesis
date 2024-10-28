```go
func Poly(xs []int, x float64) float64{
    sum := 0.0
    for i, coeff := range xs {
        sum += float64(coeff) * math.Pow(x,float64(i))
    }
    return sum
}

func FindZero(xs []int) float64 {
    if len(xs)%2 != 0 || xs[0] != 0 {
        panic("Invalid input: xs should have an even number of coefficients and the first coefficient should be zero")
    }
    // Find the largest non-zero coefficient
    maxIndex := 0
    for i := 1; i < len(xs); i += 2 {
        if xs[i] != 0 && i > maxIndex {
            maxIndex = i
        }
    }
    // Use Newton's method to find the zero
    x := float64(maxIndex) / 2.0
    for i := 0; i < 10; i++ { // 10 iterations should be enough for most cases
        x -= Poly(xs, x) / Poly(xs, x+0.00001) // Use x+0.00001 to avoid division by zero
    }
    return x
}
```

This code first checks if the input `xs` is valid (an even number of coefficients and the first coefficient is zero). Then it finds the largest non-zero coefficient, which is guaranteed to be a solution. It then uses Newton's method to find the zero of the polynomial. Newton's method iteratively refines the guess for the zero by taking the tangent of the function at the current guess and finding the root of that tangent. The code uses a small perturbation (`x+0.00001`) to avoid division by zero when calculating the derivative of the polynomial.