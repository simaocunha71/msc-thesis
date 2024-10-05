    if len(xs) % 2 == 1 {
        xs = append(xs, 0)
    }
    var x0 float64 = float64(xs[len(xs)-2]) / float64(xs[len(xs)-1])
    var eps float64 = 1e-6
    var x1 float64
    for {
        x1 = x0 - Poly(xs, x0) / Poly(xs[len(xs)-2:], x0)
        if math.Abs(x1-x0) < eps {
            return x1
        }
        x0 = x1
    }
}


