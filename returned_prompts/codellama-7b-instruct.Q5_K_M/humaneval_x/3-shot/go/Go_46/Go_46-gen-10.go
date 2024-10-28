    if n <= 0 {
        return 0
    }

    if n == 1 {
        return 0
    }

    if n == 2 {
        return 2
    }

    if n == 3 {
        return 0
    }

    var a, b, c int = 0, 0, 0
    for i := 0; i < n; i++ {
        if i == 0 {
            a = 0
            b = 0
        }
        if i == 1 {
            a = 0
            b = 0
        }
        if i == 2 {
            a = 2
            b = 0
        }
        if i == 3 {
            a = 0
            b = 0
        }
        if i > 3 {
            c = a + b
            a = b
            b = c
        }
    }
    return b
}
