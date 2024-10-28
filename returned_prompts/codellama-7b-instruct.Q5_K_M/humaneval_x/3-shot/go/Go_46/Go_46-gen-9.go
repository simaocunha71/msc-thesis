    if n == 0 {
        return 0
    }

    var a, b, c, d int = 0, 0, 2, 0

    for i := 0; i < n; i++ {
        a, b, c, d = b, c, d, a + b + c + d
    }
    return d
}



