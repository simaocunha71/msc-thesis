    n := len(xs) - 1
    a := math.Pow(-xs[n]/float64(xs[n-1]), 2)
    b := -2 * xs[n-1] * xs[n] / float64(n+1)
    c := xs[n] * xs[n] / float64(n+1)

    discriminant := b*b - 4*a*c
    if discriminant < 0 {
        return math.NaN()
    } else if discriminant == 0 {
        return -b/(2*a)
    } else {
        return (-b - math.Sqrt(discriminant)) / (2 * a)
    }
}



