    if n <= 0 {
        return 0
    }else if n == 1 {
        return 1
    }else {
        a, b := 0, 1
        for i := 2; i <= n; i++ {
            a, b = b, a+b
        }
        return b
    }
}