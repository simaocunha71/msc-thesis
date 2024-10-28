    result := 1
    for i := 1; i <= n; i++ {
        factorial := 1
        for j := 1; j <= i; j++ {
            factorial *= j
        }
        result *= factorial
    }
    return result
}



