    result := 1
    for i := 1; i <= n; i++ {
        result *= i
    }

    for i := n - 1; i >= 1; i-- {
        result *= i
    }

    return result
}