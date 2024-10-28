    left  := 0.0
    right  := 1.0
    mid  := 0.0

    for Poly(xs, left) * Poly(xs, right) > 0 {
        if right  - left < 0.00001 {
            return -1.0
        }
        mid  := (left  + right ) / 2.0

        if Poly(xs, mid) > 0 {
            right  = mid
        } else if Poly(xs, mid) < 0 {
            left  = mid
        } else {
            return mid
        }
    }

    return mid
}



