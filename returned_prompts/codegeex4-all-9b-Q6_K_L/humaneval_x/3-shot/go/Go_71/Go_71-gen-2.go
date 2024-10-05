    if a+b <= c || a+c <= b || b+c <= a {
        return -1
    }
    p := (a + b + c) / 2
    return math.Round(math.Sqrt(p * (p - a) * (p - b) * (p - c)) * 100) / 100
}

