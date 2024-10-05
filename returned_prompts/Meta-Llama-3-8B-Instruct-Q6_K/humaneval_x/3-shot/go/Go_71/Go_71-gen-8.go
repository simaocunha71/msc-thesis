    if a+b > c && a+c > b && b+c > a {
        s := (a + b + c) / 2
        return fmt.Sprintf("%.2f", math.Sqrt(math.Pow(s-a, 2) + math.Pow(s-b, 2) + math.Pow(s-c, 2)))
    } else {
        return -1
    }
}