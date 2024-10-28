    if n == 1 {
    	return 2
    }
    if n == 2 {
    	return 3
    }
    fib := make([]int, n + 1)
    fib[0] = 0
    fib[1] = 1
    for i := 2; i <= n; i++ {
        fib[i] = fib[i - 1] + fib[i - 2]
        for j := 2; j <= int(math.Sqrt(float64(fib[i]))) + 1; j++ {
            if fib[i] % j == 0 {
                break
            } else {
                if j > fib[i] {
                    return fib[i]
                }
            }
        }
    }
    return -1
}



