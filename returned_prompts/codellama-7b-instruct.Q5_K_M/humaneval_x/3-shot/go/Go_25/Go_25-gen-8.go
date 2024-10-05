    result := make([]int, 0)
    for i := 2; i < math.Sqrt(float64(n)); i++ {
        if n % i == 0 {
            result = append(result, i)
            for n % i == 0 {
                n /= i
            }
        }
    }
    if n > 1 {
        result = append(result, n)
    }
    return result
}



