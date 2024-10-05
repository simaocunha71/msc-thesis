    var derivative []int

    for i := 1; i < len(xs); i++ {
        derivative = append(derivative, i * xs[i])
    }
    return derivative
}



