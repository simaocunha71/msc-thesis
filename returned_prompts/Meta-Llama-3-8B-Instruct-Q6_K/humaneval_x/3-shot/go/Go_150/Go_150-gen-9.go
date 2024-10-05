    if isPrime(n) {
        return x
    } else {
        return y
    }
}

func isPrime(m int) bool {
    if m <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(m))); i++ {
        if m%i == 0 {
            return false
        }
    }
    return true
}