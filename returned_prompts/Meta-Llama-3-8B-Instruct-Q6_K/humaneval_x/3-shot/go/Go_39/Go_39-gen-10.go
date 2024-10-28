    a, b := 0, 1
    primeCount := 0

    for primeCount < n {
        if IsPrime(b) {
            a, b = b, a+b
            primeCount++
        } else {
            b = a + b
        }
    }
    return a
}

func IsPrime(num int) bool {
    if num <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
        if num%i == 0 {
            return false
        }
    }
    return true
}