    result := 0
    if n==1 {
        return 1
    }
    one_count := math.Pow(10, float64(n-1))
    ten_count := math.Pow(10, float64(n))
    result = int(one_count) + int(ten_count) - 1
    return result
}



