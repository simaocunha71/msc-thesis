    if n <= 2 {
        return make([]int, 0)
    }
    result := make([]int, 0)
    for i := 2; i < n; i++ {
        if isPrime(i) {
            result = append(result, i)
        }
    }
    return result
}

func isPrime(i int) bool {
    if i <= 3 {
        return i > 1
    }
    for d := 2; d * d <= i; d++ {
        if i % d == 0 {
            return false
        }
    }
    return true
}



