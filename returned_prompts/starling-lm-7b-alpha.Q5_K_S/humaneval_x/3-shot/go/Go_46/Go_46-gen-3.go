    if n == 0 || n == 1 {
        return 0
    }
    if n == 2 {
        return 2
    }
    if n == 3 {
        return 0
    }

    fib_sequence := make([]int, n+1)
    fib_sequence[0] = 0
    fib_sequence[1] = 0
    fib_sequence[2] = 2
    fib_sequence[3] = 0

    for i := 4; i <= n; i++ {
        fib_sequence[i] = fib_sequence[i-1] + fib_sequence[i-2] + fib_sequence[i-3] + fib_sequence[i-4]
    }

    return fib_sequence[n]
}



