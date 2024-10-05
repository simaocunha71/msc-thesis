    if a+b>c && b+c>a && c+a>b {
        p := (a + b + c) / 2.0
        return math.Sqrt(p * (p - a) * (p - b) * (p - c))
    }
    return -1
}



