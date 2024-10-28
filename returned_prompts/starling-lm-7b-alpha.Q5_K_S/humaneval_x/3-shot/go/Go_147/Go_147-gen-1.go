    var result int = 0
    for i := 1; i <= n; i++ {
        var tmp int = i*i - i + 1
        if tmp % 3 == 0 {
            result++
        }
    }
    return result
}



