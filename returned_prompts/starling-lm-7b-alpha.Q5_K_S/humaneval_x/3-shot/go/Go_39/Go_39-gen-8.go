    fib := make([]int, n+1)
    fib[0], fib[1] = 0, 1
    for i := 2; i <= n; i++ {
        fib[i] = fib[i-1] + fib[i-2]
        for j := 2; j*j <= fib[i]; j++ {
            if fib[i] % j == 0 {
                break
            }
            if j*j > fib[i] {
                return fib[i]
            }
        }
    }
    return -1
}



