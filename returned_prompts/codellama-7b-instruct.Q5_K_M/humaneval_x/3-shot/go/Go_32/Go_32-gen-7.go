    if len(xs) % 2 == 1 {
        panic("Polynomial should have even number of coefficients")
    }
    max_abs_coeff := 0
    for _, c := range xs {
        if max_abs_coeff < math.Abs(float64(c)) {
            max_abs_coeff = math.Abs(float64(c))
        }
    }
    if max_abs_coeff == 0 {
        panic("Polynomial should have at least one non-zero coefficient")
    }
    x := -max_abs_coeff / 2
    for i := 0; i < 100; i++ {
        if Poly(xs, x) == 0 {
            return x
        }
        x += -1.0 * Poly(xs, x) / Poly(xs, x*x)
    }
    panic("Too many iterations")
}



