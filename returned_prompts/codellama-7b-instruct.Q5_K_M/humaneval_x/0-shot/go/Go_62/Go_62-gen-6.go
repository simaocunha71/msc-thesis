
    for i := range xs {
        if i == 0 {
            continue A
        }
        xs[i-1] *= i
    }

    return xs
}
