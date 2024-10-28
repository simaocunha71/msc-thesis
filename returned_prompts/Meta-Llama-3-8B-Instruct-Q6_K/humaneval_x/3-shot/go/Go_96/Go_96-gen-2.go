    result := make([]int, 0)
    for i := 2; i < n; i++ {
        isPrime := true
        for j := 2; j <= int(math.Sqrt(float64(i))); j++ {
            if i%j == 0 {
                isPrime = false
                break
            }
        }
        if isPrime {
            result = append(result, i)
        }
    }
    return result
}