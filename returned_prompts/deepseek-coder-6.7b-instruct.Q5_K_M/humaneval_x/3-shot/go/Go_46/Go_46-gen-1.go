    if n < 4 {
        return n % 2
    }

    a, b, c, d := 0, 0, 2, 0
    for i := 4; i <= n; i++ {
        a, b, c, d = b, c, d, (a+b+c)%2
    }
    return d
}



