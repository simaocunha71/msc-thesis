    result := 1

    for i := 2; i <= n; i++ {
        if n % i == 0 {
            isPrime := true
            for j := 2; j < i; j++ {
                if i % j == 0 {
                    isPrime = false
                    break
                }
            }
            if isPrime {
                result = i
            }
        }
    }

    return result
}



