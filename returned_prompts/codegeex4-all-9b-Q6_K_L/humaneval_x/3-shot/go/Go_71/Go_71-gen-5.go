    if a + b > c && b + c > a && c + a > b {
        return math.Round((a * b * math.Sqrt(float64(1 - (a*a + b*b - c*c) * (a*a + b*b - c*c) / (4 * a * a * b * b)))) / 2 * 100) / 100
    }else{
        return -1
    }
}

