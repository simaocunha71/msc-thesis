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

    var a int = 0
    var b int = 0
    var c int = 0
    var d int = 0

    a = Fib4(n-1)
    b = Fib4(n-2)
    c = Fib4(n-3)
    d = Fib4(n-4)

    return a + b + c + d
}



