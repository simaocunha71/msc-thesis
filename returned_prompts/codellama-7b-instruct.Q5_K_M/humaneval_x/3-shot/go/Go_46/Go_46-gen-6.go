    a := 0
    b := 0
    c := 2

    for i := 0; i < n; i++ {
        a, b = b, a+b+c
    }
    return a
}



