    if n == 0 || n == 1 {
        return 0
    } else if n == 2 {
        return 1
    }
    return Fibfib(n-1) + Fibfib(n-2) + Fibfib(n-3)
}



