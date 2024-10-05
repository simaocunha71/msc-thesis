    result := make([]int, n)
    for i := range result {
        if i % 2 == 0 {
            result[i] = factorial(i)
        } else {
            result[i] = sum(i)
        }
    }
    return result
}

func factorial(n int) int {
    if n == 0 {
        return 1
    }
    return n * factorial(n-1)
}

func sum(n int) int {
    total := 0
    for i := 1; i <= n; i++ {
        total += i
    }
    return total
}


