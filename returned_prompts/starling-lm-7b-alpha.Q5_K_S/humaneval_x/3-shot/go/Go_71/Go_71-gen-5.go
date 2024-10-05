    if a + b <= c || b + c <= a || a + c <= b {
        return -1
    }
    p := (a + b + c) / 2.0
    return math.Sqrt(p * (p - a) * (p - b) * (p - c))
}



