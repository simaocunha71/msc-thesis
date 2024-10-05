    a := 0
    b := 0
    c := 2

    if n == 0 {
        return 0
    }

    for i := 1; i < n; i++ {
        a, b, c = b, c, a+b+c
    }
    return c
}



