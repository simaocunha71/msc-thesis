    var prev int
    var monotonic bool
    for _, v := range l {
        if monotonic {
            if v <= prev {
                return false
            }
        } else {
            if v >= prev {
                return false
            }
        }
        prev = v
        if v == prev {
            monotonic = !monotonic
        }
    }
    return true
}