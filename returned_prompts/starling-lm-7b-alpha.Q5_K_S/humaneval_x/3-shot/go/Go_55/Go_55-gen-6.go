    if n <= 2 {
        return 1
    }
    var fib_n_minus_one, fib_n_minus_two int = 1, 1
    for i := 2; i < n; i++ {
        fib_n_minus_one, fib_n_minus_two = fib_n_minus_two, fib_n_minus_one + fib_n_minus_two
    }
    return fib_n_minus_one
}



