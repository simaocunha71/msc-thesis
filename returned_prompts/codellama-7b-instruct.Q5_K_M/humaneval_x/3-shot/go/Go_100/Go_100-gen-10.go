    result := make([]int, n)

    for i := 0; i < n; i++ {
        result[i] = int(math.Pow(2, float64(i)))
    }
    return result
}



