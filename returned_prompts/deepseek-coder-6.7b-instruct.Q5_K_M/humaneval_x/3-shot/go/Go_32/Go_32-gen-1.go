    start := 0.0
    end := 1.0
    mid := 0.0
    for i := 0; i < 100000; i++ {
        mid = (start + end) / 2
        if Poly(xs, mid) > 0 {
            end = mid
        } else if Poly(xs, mid) < 0 {
            start = mid
        } else {
            return mid
        }
    }
    return mid
}



