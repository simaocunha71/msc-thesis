    if n < 2 {
        return 0
    }

    if n == 2 {
        return 1
    }

    a := 0
    b := 0
    c := 1
    d := 0

    for i := 3; i <= n; i++ {
        d = a + b + c
        a = b
        b = c
        c = d
    }

    return d
}



