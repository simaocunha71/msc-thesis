    for i := 0; i < 100; i++ {
        mid := (low + high) / 2.0
        if Poly(xs, mid) > 0 {
            high = mid
        } else if Poly(xs, mid