    if a+b > c && a+c > b && b+c > a {
        s := (a + b + c) / 2
        area := math.Sqrt(s*(s-a)*(s-b)*(s-c))
        return fmt.Sprintf("%.2f", area)
    }
    return -1
}