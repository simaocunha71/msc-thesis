    for i := 0; i < len(xs); i += 2 {
        x := float64(i)
        if Poly(xs, x) == 0 {
            return x
        }
    }
    return 0.0
}







