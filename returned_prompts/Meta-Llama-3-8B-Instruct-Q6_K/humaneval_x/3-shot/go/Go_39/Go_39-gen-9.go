    a, b := 0, 1
    count := 0
    for {
        a, b = b, a+b
        if math.Mod(float64(b), 1) < 1e-9 {
            if IsPrime(int(b)) {
                count++
                if count == n {
                    return int(b)
                }
            }
        }
    }
}

func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i * i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}