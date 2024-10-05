    for i  := range xs {
        xs[i] = xs[i] * i
        if i < len(xs) - 1 {
            xs = xs[i+1:]
        } else {
            xs = xs[i:]
        }
    }
    return xs
}



