    fib := 0
    a, b := 0, 1
    count := 0
    for {
        fib = a
        a, b = b, a+b
        if count == n {
            break
        }
        count++
    }
    if !IsPrime(fib) {
        for {
            a, b = b, a+b
            if IsPrime(a) {
                return a
            }
        }
    }
    return fib
}

func IsPrime(num int) bool {
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