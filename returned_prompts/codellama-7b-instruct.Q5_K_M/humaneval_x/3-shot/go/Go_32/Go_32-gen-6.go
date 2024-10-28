    n := len(xs)
    if n%2 != 0 || xs[n/2] == 0 {
        panic("invalid input")
    }
    var (
        left, right float64
        middle      float64
    )
    left = -1
    right = 2
    for {
        middle = (left + right) / 2
        if Poly(xs, middle) < 0 {
            left = middle
        }else {
            right = middle
        }
        if right - left < 0.00001 {
            break
        }
    }
    return middle
}



