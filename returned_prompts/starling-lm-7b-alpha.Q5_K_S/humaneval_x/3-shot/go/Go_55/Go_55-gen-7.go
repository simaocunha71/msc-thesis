    if n == 0 || n == 1 {
        return 1
    }
    var result int = 1
    var a, b int = 1, 1
    for i := 2; i <= n; i++ {
        result = a + b
        a, b = b, result
    }
    return result
}



