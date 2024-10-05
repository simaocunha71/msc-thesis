    for i := 2; i <= n / 2; i++ {
        if n % i == 0 {
            for j := 2; j <= n / i; j++ {
                if i % j == 0 {
                    i = -1
                    break
                }
            }
        }
    }
    return i
}



