    for i := 2; i <= math.Sqrt(float64(n)); i++ {
        if n % i == 0 {
            if isPrime(i) {
                return i
            }
            return LargestPrimeFactor(n / i)
        }
    }
    return n
}



