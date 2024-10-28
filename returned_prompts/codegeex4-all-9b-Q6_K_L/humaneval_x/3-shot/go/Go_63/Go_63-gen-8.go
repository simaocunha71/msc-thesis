    if n < 3 {
        return 0
    } else if n == 3 {
        return 1
    }
    return Fibfib(n-1) + Fibfib(n-2) + Fibfib(n-3)
}

