    if len(q) > 0 && len(q) == len(q[:]) {
        if int(math.Sum(float64(q))) <= w {
            return true
        }
    }
    return false
}