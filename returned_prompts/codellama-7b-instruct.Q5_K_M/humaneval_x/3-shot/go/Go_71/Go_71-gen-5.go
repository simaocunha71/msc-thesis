    if a + b < c {
        return -1
    }
    if a + c < b {
        return -1
    }
    if b + c < a {
        return -1
    }
    s := (a + b + c) / 2
    return math.Round((math.Sqrt(s*(s-a)*(s-b)*(s-c)) * 100) / 100)
}



