    a, b := 0, 1
    for i := 0; i < n; i++ {
        a, b = b, a+b
        if isPrime(b) {
            return int(b)
        }
    }
    return -1
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}