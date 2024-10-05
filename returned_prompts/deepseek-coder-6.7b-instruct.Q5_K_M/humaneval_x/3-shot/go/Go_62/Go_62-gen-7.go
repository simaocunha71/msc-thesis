    for i := 0; i < len(xs); i++ {
        xs[i] = xs[i] * (len(xs) - i - 1)
    }
    return xs[:len(xs)-1]
}



