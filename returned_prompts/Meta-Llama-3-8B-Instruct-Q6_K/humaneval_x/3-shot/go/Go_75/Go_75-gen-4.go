    for i := 2; i <= math.Sqrt(float64(a)); i++ {
        for j := i; j <= math.Sqrt(float64(a)); j++ {
            for k := j; k <= math.Sqrt(float64(a)); k++ {
                if i*j*k == a {
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
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}
}