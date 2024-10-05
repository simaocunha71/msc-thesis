    if a+b>c && a+c>b && b+c>a {
        p := (a+b+c) / 2
        area := math.Sqrt(p*(p-a)*(p-b)*(p-c))
        return fmt.Sprintf("%.2f", area)
    } else {
        return -1
    }
}