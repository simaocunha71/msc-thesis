    primes := []int{}
    for i := 2; i < n; i++ {
        if isPrime(i) {
            primes = append(primes, i)
        }
    }
    return primes
}

func isPrime(n int) bool {
    if n < 2 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}


