    // Ensure that xs are ordered.
    for i, coeff := range xs {
        if i > 0 && math.Abs(float64(coeff)) > math.Abs(float64(xs[i-1])) {
            xs[i], xs[i-1] = xs[i-1], xs[i]
        }
    }

    // Check if coefficients are ordered properly
    if xs[0] == 0 {
        return float64(xs[1] / xs[2])
    }

    // Ensure that xs[1] < 0
    if xs[0] > 0 && xs[1] > 0 {
        xs[0], xs[1] = xs[1], xs[0]
    } else if xs[0] < 0 && xs[1] < 0 {
        xs[0], xs[1] = xs[1], xs[0]
    }

    // Find zero for xs[1] * x + xs[0] = 0
    return -float64(xs[0]) / float64(xs[1])
}



