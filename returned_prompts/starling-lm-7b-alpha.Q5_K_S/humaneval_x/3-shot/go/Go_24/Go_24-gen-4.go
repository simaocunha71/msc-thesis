    for i := 1; i <= n / 2; i++ {
        if n % i == 0 {
            return i
        }
    }
    return n
}



