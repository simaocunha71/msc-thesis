    if n <= 3 {
        return 0
    } else if n == 4 {
        return 2
    } else {
        a, b, c, d := 0, 0, 2, 0
        for i := 5; i <= n; i++ {
            a, b, c, d = b, c, d, a+b+c
        }
        return d
    }
}