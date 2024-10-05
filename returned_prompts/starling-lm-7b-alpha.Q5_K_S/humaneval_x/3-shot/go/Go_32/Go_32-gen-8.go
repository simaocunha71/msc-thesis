    n := len(xs)
    xs_norm := make([]float64,n)
    for i, coeff := range xs {
        xs_norm[i] = float64(coeff) / math.Pow(float64(n-i), n)
    }
    result := Poly(xs_norm, -1)
    return result
}



