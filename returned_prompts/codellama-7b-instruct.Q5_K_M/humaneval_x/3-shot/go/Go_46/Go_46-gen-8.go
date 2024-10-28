    if n <= 1 {
        return 0
    }

    if n == 2 {
        return 2
    }

    if n == 3 {
        return 0
    }

    return Fib4(n-1) + Fib4(n-2) + Fib4(n-3) + Fib4(n-4)
}



