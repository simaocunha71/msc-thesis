    if n == 0 || n == 1 {
        return 0
    }

    a, b := 0, 2
    for i := 2; i < n; i++ {
        a, b = b, a+b
    }

    return b
}



