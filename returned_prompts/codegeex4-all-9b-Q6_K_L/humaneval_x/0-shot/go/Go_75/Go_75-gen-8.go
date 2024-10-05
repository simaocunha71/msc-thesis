func IsMultiplyPrime(a int) bool {
    if a < 2 {
        return false
    }
    var primeFactors []int
    for i := 2; i <= a; i++ {
        for a%i == 0 {
            primeFactors = append(primeFactors, i)
            a = a / i
        }
    }
    if len(primeFactors) != 3 {
        return false
    }
    for _, factor := range primeFactors {
        if !isPrime(factor) {
            return false
        }
    }
    return true
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
