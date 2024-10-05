    if a+b>c && b+c>a && c+a>b {
        s := (a+b+c) / 2
        return math.Round(math.Sqrt(s * (s - a) * (s - b) * (s - c)) * 100) / 100
    }
    return -1
}



