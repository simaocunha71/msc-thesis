    if n == 0 {
        return 0
    }
    if n == 1 {
        return 0
    }
    if n == 2 {
        return 1
    }

    a, b, c := 0, 0, 1
    var d int
    for i := 3; i <= n; i++ {
        d = a + b + c
        a, b, c = b, c, d
    }

    return d
}



