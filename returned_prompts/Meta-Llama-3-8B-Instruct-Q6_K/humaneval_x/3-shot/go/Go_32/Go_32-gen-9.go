    if len(xs)%2==0 {
        sum := 0.0
        for i, coeff := range xs {
            sum += float64(coeff) * math.Pow(-1, i/2) * math.Pow(float64(len(xs)/2-i), 1)
        }
        return sum
    } else {
        panic("FindZero only takes list xs having even number of coefficients")
    }
}