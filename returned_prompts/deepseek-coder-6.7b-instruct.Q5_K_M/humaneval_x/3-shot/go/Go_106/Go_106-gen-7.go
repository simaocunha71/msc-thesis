    result := make([]int, n)

    for i := 0; i < n; i++ {
        if i % 2 == 0 {
            result[i] = factorial(i+1)
        } else {
            result[i] = sum(i+1)
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
    return n * (n + 1) / 2
}



