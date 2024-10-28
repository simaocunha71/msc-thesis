    var maxFactor int
    for i := n / 2; i > 1; i-- {
        if n%i == 0 {
            isPrime := true
            for j := 2; j*j <= i; j++ {
                if i % j == 0 {
                    isPrime = false
                    break
                }
            }
            if isPrime {
                maxFactor = i
            }
        }
    }
    return maxFactor
}