    var a, b, c, d int = 0, 0, 2, 0
    for i:=0; i<n; i++{
        c, d = a+c, b+d
        a, b = c, d
    }
    return b
}



