    result := make([]int, 0)
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        for n % i == 0 {
            result = append(result, i)
            n /= i
        }
    }
    if n > 1 {
        result = append(result, n)
    }
    return result
}



