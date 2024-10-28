    if n == 0 || n == 1 {
        return 0
    }

    if n == 2 {
        return 2
    }

    if n == 3 {
        return 0
    }

    var fib4s = make([]int, n+1)
    fib4s[0] = 0
    fib4s[1] = 0
    fib4s[2] = 2
    fib4s[3] = 0

    for i := 4; i <= n; i++ {
        fib4s[i] = fib4s[i-1] + fib4s[i-2] + fib4s[i-3] + fib4s[i-4]
    }

    return fib4s[n]
}

