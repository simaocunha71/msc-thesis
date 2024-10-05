    a, b := 0, 1
    for i := 0; i < n; i++ {
        a, b = b, a+b
        if IsPrime(a) {
            return a
        }
    }
    return 0
}



