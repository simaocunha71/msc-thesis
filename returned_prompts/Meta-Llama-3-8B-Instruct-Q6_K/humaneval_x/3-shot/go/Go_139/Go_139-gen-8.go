    result := 1
    for i := 1; i <= n; i++ {
        var temp int = 1
        for j := 1; j <= i; j++ {
            temp *= j
        }
        result *= temp
    }
    return result
} 