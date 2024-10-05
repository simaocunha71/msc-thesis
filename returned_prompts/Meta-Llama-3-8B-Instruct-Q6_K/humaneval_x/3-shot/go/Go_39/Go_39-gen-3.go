    a, b := 0, 1
    count := 0
    for {
        a, b = b, a+b
        if math.Mod(float64(b), 2) == 0 {
            continue
        }
        if isPrime(b) {
            count++
            if count == n {
                return int(b)
            }
        }
    }
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if math.Mod(float64(n), float64(i)) == 0 {
            return false
        }
    }
    return true
}