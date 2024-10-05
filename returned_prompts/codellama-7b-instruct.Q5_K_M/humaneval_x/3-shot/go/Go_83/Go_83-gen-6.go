    var result int

    if n == 1 {
        return 1
    }

    for i := 1; i < n; i++ {
        result += int(math.Pow(10, float64(i))) * 2
    }
    result += int(math.Pow(10, float64(n)))

    return result
}



