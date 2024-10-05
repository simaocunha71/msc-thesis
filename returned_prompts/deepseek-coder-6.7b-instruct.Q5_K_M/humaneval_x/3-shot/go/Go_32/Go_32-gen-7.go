    var a, b float64 = 0, 100
    for math.Abs(a - b) > 1e-6 {
        c := (a + b) / 2
        if Poly(xs, c) > 0 {
            b = c
        } else {
            a = c
        }
    }
    return a
}


