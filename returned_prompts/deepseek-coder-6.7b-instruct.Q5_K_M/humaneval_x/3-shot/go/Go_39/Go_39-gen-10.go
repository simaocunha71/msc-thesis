    primes, fibs := make([]int, 0), make([]int, 0)
    fibs = append(fibs, 1, 2)
    primes = append(primes, 2)

    for i := 3; len(primes) <= n; i += 2 {
        if isPrime(i) {
            primes = append(primes, i)
        }
        fibs = append(fibs, fibs[len(fibs)-1]+fibs[len(fibs)-2])
    }

    return primes[n-1]
}

func isPrime(n int) bool {
    if n % 2 == 0 {
        return false
    }

    sqrt := int(math.Sqrt(float64(n)))
    for i := 3; i <= sqrt; i += 2 {
        if n % i == 0 {
            return false
        }
    }
    return true
}

