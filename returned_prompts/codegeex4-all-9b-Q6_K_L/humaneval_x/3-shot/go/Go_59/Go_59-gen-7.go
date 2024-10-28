    for i := 2; i <= n; i++ {
        if n%i == 0 {
            for n%i == 0 {
                n = n / i
            }
            if n == 1 {
                return i
            }
        }
    }
    return n
}



