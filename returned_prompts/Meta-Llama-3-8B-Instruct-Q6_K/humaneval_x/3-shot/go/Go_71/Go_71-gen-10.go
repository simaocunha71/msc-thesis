    if a+b>c && a+c>b && b+c>a {
        return math.Sqrt(math.Pow((a+b-c)/2)*math.Pow((a+b-c)/2-math.Pow(c,2)/4)*math.Pow((a-b+c)/2-math.Pow(c,2)/4))
    } else {
        return -1
    }
}