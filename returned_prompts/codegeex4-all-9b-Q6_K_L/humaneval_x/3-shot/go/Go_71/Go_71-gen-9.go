    if a+b <= c || b+c <= a || a+c <= b {
        return -1
    } else {
        s := (a + b + c) / 2
        area := math.Sqrt(s * (s - a) * (s - b) * (s - c))
        return math.Round(area*100)/100
    }
}



