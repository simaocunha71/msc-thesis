    if n == 0 || n == 1 {
        return 0
    }
    if n == 2 {
        return 1
    }
    var result int = 0
    for i := 3; i <= n; i++ {
        result = Fibfib(i-1) + Fibfib(i-2) + Fibfib(i-3)
    }
    return result
}

