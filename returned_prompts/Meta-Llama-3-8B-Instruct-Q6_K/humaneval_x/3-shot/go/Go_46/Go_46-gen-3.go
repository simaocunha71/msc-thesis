    if n <= 3 {
        return 0
    }
    if n == 4 {
        return 2
    }
    fib4 := make([]int, n+1)
    fib4[1] = 0
    fib4[2] = 2
    fib4[3] = 0
    for i := 4; i <= n; i++ {
        fib4[i] = fib4[i-1] + fib4[i-2] + fib4[i-3] + fib4[i-4]
    }
    return fib4[n]
}