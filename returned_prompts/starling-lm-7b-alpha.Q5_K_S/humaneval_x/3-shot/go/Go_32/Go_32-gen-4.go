    n := len(xs)
    sum := 0.0
    for i := 0; i < n; i++ {
        sum += float64(xs[i]) * math.Pow(-1,float64(i))
    }
    return -sum/float64(n)
}



