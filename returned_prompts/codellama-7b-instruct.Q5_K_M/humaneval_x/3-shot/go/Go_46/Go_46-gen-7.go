    if n == 0 || n == 1{
        return 0
    }
    if n == 2{
        return 2
    }
    if n == 3{
        return 0
    }
    var a, b, c, d int = 0,0,0,0
    a = 0
    b = 0
    c = 2
    d = 0
    for i := 4; i <= n; i++{
        a = b
        b = c
        c = d
        d = a + b + c
    }
    return d
}



