    if len(xs)%2!=0{
        return 0
    }
    a := float64(xs[0])
    b := float64(xs[1])
    for i := 2; i < len(xs); i += 2 {
        c := float64(xs[i])
        d := float64(xs[i+1])
        a, b = b, b*b - 4*a*c
    }
    return -b/(2*a)
}  // Newton-Raphson method
}  // package main



