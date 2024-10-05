    if n == 0 {
        return 1
    } else if n == 1 {
        return 2
    } else {
        return 2 * int(math.Pow(10, float64(n-2)))
    }
}



