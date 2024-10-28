    if a + b <= c || a + c <= b || b + c <= a {
        return -1
    }
    s := (a + b + c) / 2
    return math.Round(math.Sqrt(s * (s - a) * (s - b) * (s - c)) * 100) / 100
}