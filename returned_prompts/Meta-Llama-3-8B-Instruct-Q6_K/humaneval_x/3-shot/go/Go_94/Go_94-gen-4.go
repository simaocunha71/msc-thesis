    maxPrime := 0
    for _, n := range lst {
        if isPrime(n) && n > maxPrime {
            maxPrime = n
        }
    }
    return sumDigits(maxPrime)
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

func sumDigits(n int) int {
    sum := 0
    for n > 0 {
        sum += n % 10
        n /= 10
    }
    return sum
}