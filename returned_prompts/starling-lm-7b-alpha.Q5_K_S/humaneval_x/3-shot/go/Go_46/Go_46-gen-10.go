    if n < 4 {
        return 0
    }
    if n == 4 {
        return 2
    }
    a, b, c, d := 0, 0, 2, 0
    for i := 4; i <= n; i++ {
        a, b, c, d = b, c, d+b+a, a
    }
    return d
}



