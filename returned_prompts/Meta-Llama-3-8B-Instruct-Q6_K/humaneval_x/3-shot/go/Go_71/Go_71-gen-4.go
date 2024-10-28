    if a+b > c && a+c > b && b+c > a {
        s := (a + b + c) / 2
        area := math.Sqrt(s * (s - a) * (s - b) * (s - c))
        return math.Round(area * 100) / 100
    } else {
        return -1
    }
}