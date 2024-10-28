    a, b := 0, 1
    for i := 0; i < n; i++ {
        a, b = b, a+b
        if isPrime(b) {
            return int(b)
        }
    }
    return 0
}

func isPrime(num int) bool {
    if num < 2 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
        if num%i == 0 {
            return false
        }
    }
    return true
}