    var zero float64 = 0
    for _, coeff := range xs {
        zero += float64(coeff)
    }
    return zero / float64(len(xs))
}

