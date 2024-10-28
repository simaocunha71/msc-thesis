    if n <= 1{
        return n
    }
    var a, b int = 0, 2
    for i := 3; i <= n; i++ {
        a, b = b, a + b
    }
    return b
}



