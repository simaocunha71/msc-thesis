    var p float64 = (a + b + c) / 2
    var area float64 = math.Sqrt(p * (p - a) * (p - b) * (p - c))
    var result float64 = area
    if math.Mod(area, 1) != 0 || a + b <= c || a + c <= b || b + c <= a {
        result = -1
    }
    return result
}



