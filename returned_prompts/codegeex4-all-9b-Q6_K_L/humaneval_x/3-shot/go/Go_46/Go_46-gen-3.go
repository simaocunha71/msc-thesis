    if n == 0 || n == 1 {
        return 0
    } else if n == 2 {
        return 2
    } else {
        fib := make([]int, n+1)
        fib[0] = 0
        fib[1] = 0
        fib[2] = 2
        fib[3] = 0
        for i := 4; i <= n; i++ {
            fib[i] = fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4]
        }
        return fib[n]
    }
}

