    if n <= 3 {
        switch n {
        case 0:
            return 0
        case 1:
            return 0
        case 2:
            return 2
        case 3:
            return 0
        }
    }

    a, b, c, d := 0, 0, 2, 0
    for i := 4; i <= n; i++ {
        a, b, c, d = b, c, d, a+b+c
    }
    return d
}