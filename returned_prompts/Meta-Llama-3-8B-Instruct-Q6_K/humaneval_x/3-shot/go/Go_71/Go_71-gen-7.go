    if a+b>c && a+c>b && b+c>a {
        return math.Round(math.Sqrt((a * (b * c - b * b - c * c) + b * (a * a - a * a - b * b) + c * (a * a - a * a - c * c)) / (2 * math.Sqrt(a*a+b*b+c*c))))*100/100.0
    } else {
        return -1
    }
}