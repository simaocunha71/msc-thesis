    var primes []int 
    var fibs []int 
    fibs = append(fibs, 1)
    fibs = append(fibs, 2)

    for i := 3; len(primes) < n; i++  {
        fibs = append(fibs, fibs[i-2] + fibs[i-3])
        if isPrime(i)  {
            primes = append(primes, i)
        }
    }
    return primes[n-1]
}

func isPrime(n int) bool  {
    if n == 2  {
        return true
    }
    if n % 2 == 0  {
        return false
    }
    sqrtn := int(math.Sqrt(float64(n)))
    for i := 3; i <= sqrtn; i += 2  {
        if n % i == 0  {
            return false
        }
    }
    return true
}



