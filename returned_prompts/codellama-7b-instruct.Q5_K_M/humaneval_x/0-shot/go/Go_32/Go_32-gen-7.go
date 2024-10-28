    if len(xs)%2 == 0 {
        max := 0
        for i := 1; i < len(xs); i += 2 {
            if xs[i] > max {
                max = xs[i]
            }
        }
        if max == 0 {
            // all coefficients are 0
            return 0
        }
        return -max
    }
    xs = append(xs, 0)
    goto A
}
