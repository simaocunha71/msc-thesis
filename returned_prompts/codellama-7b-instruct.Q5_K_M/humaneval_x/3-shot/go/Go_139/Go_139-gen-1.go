    var result int = 1
    for i := 1; i <= n; i++ {
        result *= (i * (n - i))
    }
    return result
}



