    if n < 2 {
        return []int{}
    }

    sieve := make([]bool, n+1)
    for i := range sieve {
        sieve[i] = true
    }

    for p := 2; p*p <= n; p++ {
        if sieve[p] {
            for i := p * p; i <= n; i += p {
                sieve[i] = false
            }
        }
    }

    primes := make([]int, 0, n)
    for p := 2; p <= n; p++ {
        if sieve[p] {
            primes = append(primes, p)
        }
    }

    return primes
}



