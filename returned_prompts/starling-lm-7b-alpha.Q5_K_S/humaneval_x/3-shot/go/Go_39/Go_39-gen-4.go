    fib := 0
    fib_prev := 1
    fib_prev_prev := 0
    for i := 0; i < n; i++ {
        fib = fib_prev_prev + fib_prev
        fib_prev_prev = fib_prev
        fib_prev = fib
        if fib_prev_prev != 1 && fib_prev != 2 {
            break
        }
    }

    for i := 2; i <= int(math.Sqrt(float64(fib))); i++ {
        if fib % i == 0 {
            return PrimeFib(n+1)
        }
    }
    return fib
}



