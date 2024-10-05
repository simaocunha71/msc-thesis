    if len(xs) % 2 == 1 {
        xs = append(xs, 0)
    }

    max := 0
    for i, coeff := range xs {
        if coeff > max {
            max = coeff
        }
        if i > max {
            break A
        }
    }
    var x float64 = -1
    var prev float64 = -1
    for i := 0; i < max; i++ {
        x = prev + 0.01
        if Poly(xs, x) < 0 {
            if prev == x {
                return prev
            }
            return x
        }
        prev = x
    }
    return -1
}
