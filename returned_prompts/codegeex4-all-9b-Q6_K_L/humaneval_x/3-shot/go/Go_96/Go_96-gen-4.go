    result := make([]int, 0)

    if n < 2 {
        return result
    }

    for i := 2; i < n; i++ {
        isPrime := true
        for j := 2; j < i; j++ {
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

