    if n == 0 {
        return 0
    } else if n == 1 {
        return 0
    } else if n == 2 {
        return 2
    } else if n == 3 {
        return 0
    } else {
        fib4_0 := 0
        fib4_1 := 0
        fib4_2 := 2
        fib4_3 := 0
        for i := 4; i <= n; i++ {
            fib4 := fib4_0 + fib4_1 + fib4_2 + fib4_3
            fib4_0 = fib4_1
            fib4_1 = fib4_2
            fib4_2 = fib4_3
            fib4_3 = fib4
        }
        return fib4_3
    }
}



