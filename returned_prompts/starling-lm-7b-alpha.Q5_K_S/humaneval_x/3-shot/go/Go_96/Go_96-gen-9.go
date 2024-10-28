    result := make([]int, 0)
    isPrime := make([]bool, n + 1)
    for i := 0; i < n + 1; i++ {
        isPrime[i] = true
    }
    isPrime[0] = false
    isPrime[1] = false
    for i := 2; i < n + 1; i++ {
        if isPrime[i] {
            for j := i * 2; j < n + 1; j += i {
                isPrime[j] = false
            }
        }
    }
    for i := 2; i < n + 1; i++ {
        if isPrime[i] {
            result = append(result, i)
        }
    }
    return result
}



