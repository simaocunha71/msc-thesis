    if n < 4{
        switch n{
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

    var a int = 0
    var b int = 0
    var c int = 2
    var d int = 0
    var result int = 0

    for i := 4; i <= n; i++{
        result = a + b + c + d
        a = b
        b = c
        c = d
        d = result
    }

    return result
}



