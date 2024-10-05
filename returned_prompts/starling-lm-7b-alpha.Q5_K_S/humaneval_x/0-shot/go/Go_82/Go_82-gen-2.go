
func PrimeLength(s string) bool {
    length := len(s)
    if length == 1 {
        return true
    }
    for i := 2; i*i <= length; i++ {
        if length%i == 0 {
            return false
        }
    }
    return true
}

    // Find all prime numbers less than length
    primes := make([]int, 0)
    for i := 2; i <= length; i++ {
        if isPrime(i) {
            primes = append(primes, i)
        }
    }

    // Check if length is one of the prime numbers
    for _, prime := range primes {
        if length == prime {
            return true
        }
    }

    return false
}

func isPrime(n int) bool {
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

*/








































































































































































































































































