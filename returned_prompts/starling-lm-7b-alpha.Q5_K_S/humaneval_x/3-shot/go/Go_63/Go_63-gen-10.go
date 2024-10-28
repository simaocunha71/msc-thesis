    if n == 0 {
        return 0
    } else if n == 1 {
        return 0
    } else if n == 2 {
        return 1
    }

    var a, b, c int = 0, 0, 1
    for i := 3; i <= n; i++ {
        c = a + b
        a = b
        b = c
    }
    return c
}



