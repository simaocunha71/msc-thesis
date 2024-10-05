    for i := n - 1; i > 1; i-- {
        if n%i == 0 {
            isPrime := true
            for j := 2; j < i; j++ {
                if i%j == 0 {
                    isPrime = false
                    break
                }
            }
            if isPrime {
                return i
            }
        }
    }
    return 1
}



