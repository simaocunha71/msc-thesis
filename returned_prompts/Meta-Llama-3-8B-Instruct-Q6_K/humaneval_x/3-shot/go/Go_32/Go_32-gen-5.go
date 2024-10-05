    if len(xs)%2 != 0{
        panic("xs must have even number of coefficients")
    }
    if xs[0] == 0{
        return 0
    }
    x := 1.0
    for xs[len(xs)-1] * math.Pow(x, float64(len(xs)-1)) != -xs[0] {
        x += 0.1
    }
    return x
}