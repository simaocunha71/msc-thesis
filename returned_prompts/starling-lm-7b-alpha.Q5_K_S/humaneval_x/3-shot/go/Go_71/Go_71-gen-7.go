    if a + b <= c || b + c <= a || c + a <= b {
        return -1
    }
    p := (a + b + c) / 2
    area := math.Sqrt(p * (p - a) * (p - b) * (p - c))
    return math.Round(area * 100) / 100
}



