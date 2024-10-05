    if a + b > c && b + c > a && a + c > b {
        s := (a + b + c) / 2
        return math.Trunc(math.Sqrt(s * (s - a) * (s - b) * (s - c)))
    }
    return -1
}



