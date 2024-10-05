    if n == 0 {
        return 0
    } else if n == 1 {
        return 0
    } else if n == 2 {
        return 2
    } else if n == 3 {
        return 0
    }

    a, b, c, d := 0, 0, 2, 0
    var e int
    for i := 4; i <= n; i++ {
        e = a + b + c + d
        a, b, c, d = b, c, d, e
    }

    return e
}



