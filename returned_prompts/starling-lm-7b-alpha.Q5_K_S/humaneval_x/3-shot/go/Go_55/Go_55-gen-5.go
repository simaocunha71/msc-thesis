    if n <= 2 {
        return 1
    }
    var fib_n_minus_2, fib_n_minus_1 int = 1, 1
    for i := 2; i < n; i++ {
        fib_n_minus_2, fib_n_minus_1 = fib_n_minus_1, fib_n_minus_1 + fib_n_minus_2
    }
    return fib_n_minus_1
}



