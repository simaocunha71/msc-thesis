    for x := 1.0; x < 10000; x++ {
        if Poly(xs, x) == 0 {
            return x
        }
    }
    return -1
}































