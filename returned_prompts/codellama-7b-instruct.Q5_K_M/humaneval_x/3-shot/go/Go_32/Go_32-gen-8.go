    if len(xs)%2 == 1 || len(xs) == 1{
        panic("xs must have even number of coefficients and at least 2")
    }
    for i := 0; i < len(xs)-2; i++ {
        if xs[i] != 0 {
            return float64(-xs[i+1]/xs[i])
        }
    }
    return 0.0
}



