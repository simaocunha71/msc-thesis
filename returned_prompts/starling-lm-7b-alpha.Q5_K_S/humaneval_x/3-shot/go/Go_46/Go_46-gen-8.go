    if n == 0 {
        return 0
    }
    if n == 1 {
        return 0
    }
    if n == 2 {
        return 2
    }
    if n == 3 {
        return 0
    }

    var fib_n_minus_1 = 0
    var fib_n_minus_2 = 2
    var fib_n_minus_3 = 0
    var fib_n_minus_4 = 0
    var fib_n = 0

    for i := 5; i <= n; i++ {
        fib_n = fib_n_minus_1 + fib_n_minus_2 + fib_n_minus_3 + fib_n_minus_4
        fib_n_minus_4 = fib_n_minus_3
        fib_n_minus_3 = fib_n_minus_2
        fib_n_minus_2 = fib_n_minus_1
        fib_n_minus_1 = fib_n
    }

    return fib_n
}



