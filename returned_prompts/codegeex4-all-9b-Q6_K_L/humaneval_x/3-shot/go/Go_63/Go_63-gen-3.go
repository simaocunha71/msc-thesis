    if n == 0 || n == 1 {
        return 0
    }
    if n == 2 {
        return 1
    }
    fibfib := make([]int, n+1)
    fibfib[0] = 0
    fibfib[1] = 0
    fibfib[2] = 1
    for i := 3; i <= n; i++ {
        fibfib[i] = fibfib[i-1] + fibfib[i-2] + fibfib[i-3]
    }
    return fibfib[n]
}

