    n := len(xs)
    if n%2 == 1 {
        panic("uneven number of coefficients")
    }
    a := float64(math.Abs(xs[n-1]))
    b := float64(math.Abs(xs[n-2]))
    return (-a + math.Sqrt(a*a+4*b*b)) / (2 * b)
}



