    var start float64 = -1000.0
    var end float64 = 1000.0
    var mid float64

    for math.Abs(start-end) > 0.00001 {
        mid = (start + end) / 2.0
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

