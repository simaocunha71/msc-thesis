func Fib(n int) int {
    if n < 2 {
        return n
    }
    return Fib(n-1) + Fib(n-2)
}

func Fib(n int) int {
    a, b := 0, 1
    for i := 0; i < n; i++ {
        a, b = b, a+b
    }
    return a
}

func Fib(n int) int {
    if n == 0 {
        return 0
    } else if n == 1 {
        return 1
    } else {
        return Fib(n-1) + Fib(n-2)
    }
}

func Fib(n int) int {
    if n < 0 {
        return -1
    }
    return fib(n)
}

func fib(n int) int {
    if n < 2 {
        return n
    }
    return fib(n-1) + fib(n-2)
}

func Fib(n int) int {
    if n < 2 {
        return n
    }
    a, b := 0, 1
    for i := 0; i < n; i++ {
        a, b = b, a+b
    }
    return b
}

func Fib(n int) int {
    if n == 0 {
        return 0
    } else if n == 1 {
        return 1
    } else {
        return Fib(n-1) + Fib(n-2)
    }
}

func Fib(n int) int {
    if n < 0 {
        return -1
    }
    return fib(n)
}

func fib(n int) int {
    if n < 2 {
        return n
    }
    return fib(n-1) + fib(n-2)
}

func Fib(n int) int {
    if n < 2 {
        return n
    }
    a, b := 0, 1
    for i := 0; i < n; i++ {
        a, b = b, a+b
    }
    return b
}

func Fib(n int) int {
    if n == 0 {
        return 0
    } else if n == 1 {
        return 1
    } else {
        return Fib(n-1) + Fib(n-2)
    }
}

func Fib(n int) int {
    if n < 0 {
        return -1
    }
    return fib