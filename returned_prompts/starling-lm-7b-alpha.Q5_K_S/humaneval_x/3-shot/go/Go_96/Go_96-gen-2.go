    result := make([]int, 0)
    for i := 2; i < n; i++ {
        if isPrime(i) {
            result = append(result, i)
        }
    }
    return result
}



