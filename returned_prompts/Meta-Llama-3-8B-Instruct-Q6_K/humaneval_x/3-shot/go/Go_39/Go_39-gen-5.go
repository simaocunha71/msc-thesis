    a, b := 0, 1
    i := 0

    for {
        a, b = b, a+b
        i++
        if i == n {
            if IsPrime(b) {
                return int(b)
            } else {
                return PrimeFib(n+1)
            }
        }
    }
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