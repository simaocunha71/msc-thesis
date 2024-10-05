    for i := 2; i < 100; i++ {
        for j := i; j < 100; j++ {
            for k := j; k < 100; k++ {
                if a == i * j * k {
                    if IsPrime(i) && IsPrime(j) && IsPrime(k) {
                        return true
                    }
                }
            }
        }
    }
    return false
}

func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}