    result := make([]int, 0)
    if n == 1 {
        return result
    }
    for i := 2; i < int(math.Sqrt(float64(n))); i++ {
        if n % i == 0 {
            result = append(result, i)
            result = append(result, Factorize(n/i)...)
            return result
        }
    }
    result = append(result, n)
    return result
}



