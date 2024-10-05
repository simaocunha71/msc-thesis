    if n < 4 {
        return n % 2
    }

    a, b, c, d := 0, 0, 2, 0
    var e int

    for i := 4; i <= n; i++ {
        e = a + b + c + d
        a, b, c, d = b, c, d, e
    }

    return e
}



