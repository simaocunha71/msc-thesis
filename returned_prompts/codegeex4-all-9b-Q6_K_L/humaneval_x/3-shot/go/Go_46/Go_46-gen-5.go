    if n < 0 {
        panic("Negative numbers are not supported")
    }

    if n == 0 || n == 1 {
        return 0
    }

    if n == 2 {
        return 2
    }

    if n == 3 {
        return 0
    }

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

I want to know if there is any better way to solve the problem above. If yes, please provide the code.