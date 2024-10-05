    if a+b>c && a+c>b && b+c>a {
        p := (a + b + c) / 2
        area := math.Sqrt(p * (p - a) * (p - b) * (p - c))
        return float64(math.Round(float64(area)*100))/100
    } else {
        return -1
    }
}