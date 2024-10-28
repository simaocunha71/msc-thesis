    i := 2
    for n % i == 0 {
        n /= i
    }
    for i = 2; i * i <= n; i++ {
        for n % i == 0 {
            n /= i
        }
    }
    return n
}