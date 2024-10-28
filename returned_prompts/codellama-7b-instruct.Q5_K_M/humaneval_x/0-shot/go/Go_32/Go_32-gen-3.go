    if len(xs)%2 == 1 {
        panic("xs must have even number of coefficients")
    }
    max := 0
    for i := range xs {
        if xs[i] > max {
            max = xs[i]
        }
    }
    if max == 0 {
        panic("all coefficients must be non zero")
    }

    // find x such that Poly(x) = 0
    x := -max
    for {
        fx := Poly(xs, x)
        if fx == 0 {
            break
        }
        x += fx / (Poly(xs, x) / math.Pow(x, float64(len(xs)-1)))
    }
    return x
}
