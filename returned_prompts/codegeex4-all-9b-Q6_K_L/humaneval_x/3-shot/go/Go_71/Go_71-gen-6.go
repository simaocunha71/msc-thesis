    if a + b > c && b + c > a && c + a > b {
        return math.Sqrt((a + b + c) * (a + b - c) * (b + c - a) * (c + a - b)) / 4
    }else {
        return -1
    }
}



