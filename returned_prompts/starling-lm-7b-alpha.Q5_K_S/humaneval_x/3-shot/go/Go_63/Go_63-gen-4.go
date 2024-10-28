    if n == 0 || n == 1 || n == 2 {
        return 0
    }
    fibs := make([]int, n+1)
    fibs[0] = 0
    fibs[1] = 0
    fibs[2] = 1
    for i := 3; i <= n; i++ {
        fibs[i] = fibs[i-1] + fibs[i-2] + fibs[i-3]
    }
    return fibs[n]
}



