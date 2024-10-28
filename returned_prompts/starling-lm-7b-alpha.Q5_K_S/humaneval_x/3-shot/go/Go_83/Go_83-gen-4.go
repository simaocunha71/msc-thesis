    result := 0

    for i := 1; i <= n; i++ {
        result += math.Pow(10,float64(i-1))
    }

    for i := 1; i <= n; i++ {
        result -= math.Pow(10,float64(i-1))
    }

    return result
}



