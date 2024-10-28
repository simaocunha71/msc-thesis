    var primes []int
    var fibs []int
    fibs = append(fibs, 1, 1)
    primes = append(primes, 2)

    for i := 2; len(primes) <= n; i++ {
        fibs = append(fibs, fibs[i-1]+fibs[i-2])
        if isPrime(fibs[i]) {
            primes = append(primes, fibs[i])
        }
    }
    return primes[n-1]
}

func isPrime(n int) bool {
    if n == 1 {
        return false
    }
    sqrtn := int(math.Sqrt(float64(n)))
    for i := 2; i <= sqrtn; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}



