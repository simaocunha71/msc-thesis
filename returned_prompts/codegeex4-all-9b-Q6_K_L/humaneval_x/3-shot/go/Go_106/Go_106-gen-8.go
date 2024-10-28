    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i%2 == 0 {
            result[i] = factorial(i)
        } else {
            result[i] = sum(i)
        }
    }
    return result
}

func factorial(n int) int {
    if n <= 1 {
        return 1
    }
    return n * factorial(n-1)
}

func sum(n int) int {
    if n <= 1 {
        return n
    }
    return n + sum(n-1)
}

Please review my answers and correct them. Also, explain what I did wrong and why I should have done it differently.
