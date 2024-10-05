    if n == 1 {
        return 2
    }
    a, b := 1, 2
    for i := 3; i <= n; i++ {
        a, b = b, a+b
        if b > 0 && b % 2 != 0 {
            for j := 2; j * j <= b; j++ {
                if b % j == 0 {
                    break
                }
            }
            if j * j > b {
                return b
            }
        }
    }
    return 0
}



