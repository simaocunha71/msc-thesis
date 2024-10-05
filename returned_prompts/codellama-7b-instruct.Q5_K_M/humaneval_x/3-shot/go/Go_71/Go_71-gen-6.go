    if (a + b) <= c || (a + c) <= b || (b + c) <= a {
        return -1
    }
    return math.Round(math.Abs((a * b * c) / (4 * math.Tan(math.Pi / 3))), 2)
}



