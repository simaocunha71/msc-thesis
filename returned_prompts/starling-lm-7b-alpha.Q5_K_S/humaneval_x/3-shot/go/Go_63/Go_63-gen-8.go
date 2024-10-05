    if n <= 2 {
        return 0
    }
    if n == 3 {
        return 1
    }
    a, b, c := 0, 1, 1
    for i := 4; i <= n; i++ {
        c = a + b
        a = b
        b = c
    }
    return c
}



