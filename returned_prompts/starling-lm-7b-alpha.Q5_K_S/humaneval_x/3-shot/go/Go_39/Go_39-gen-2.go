    if n == 1 {
        return 2
    }
    if n == 2 {
        return 3
    }
    a, b := 2, 3
    for i := 3; i <= n; i++ {
        a, b = b, a+b
        if b > 1 && IsPrime(b) {
            return b
        }
    }
    return -1
}



