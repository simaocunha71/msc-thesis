    if len(xs) % 2 == 1 {
        xs = append(xs, 0)
    }
    var x0, x1 float64 = 0, 1
    for i := 0; i < len(xs); i += 2 {
        if xs[i] == 0 {
            continue
        }
        var k float64 = float64(xs[i]) / float64(xs[i+1])
        x1 = x0 - (Poly(xs, x0) / Poly(xs, x1))
        x0 = x1
    }
    return x0
}



