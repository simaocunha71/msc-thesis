    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i % 2 == 0 {
            result[i] = factorial(i)
        } else {
            result[i] = sumFrom1To(i)
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

func sumFrom1To(n int) int {
    result := 0
    for i := 1; i <= n; i++ {
        result += i
    }
    return result
}