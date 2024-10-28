    if len(xs) % 2 == 1 || xs[0] == 0 {
        panic("Coefficients must be even and non zero")
    }
    x0 := -xs[1] / xs[0]
    x1 := x0 - (Poly(xs, x0) / Poly(xs[2:], x0))
    for math.Abs(x1 - x0) > 1e-6 {
        x0 = x1
        x1 = x0 - (Poly(xs, x0) / Poly(xs[2:], x0))
    }
    return x1
}


