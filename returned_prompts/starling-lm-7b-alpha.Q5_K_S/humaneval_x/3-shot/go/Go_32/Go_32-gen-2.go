    n := len(xs)
    if n % 2 != 0 {
        panic("FindZero only works for polynomials with even coefficients")
    }
    coeff := xs[n / 2]
    if coeff == 0 {
        panic("FindZero only works for polynomials with non zero largest coefficient")
    }
    return math.Sqrt(math.Abs(float64(coeff)) / float64(xs[n-1]))
}



