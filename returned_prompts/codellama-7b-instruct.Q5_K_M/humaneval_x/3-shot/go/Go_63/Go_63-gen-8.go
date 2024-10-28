    if n <= 1 {
        return 0
    }

    first := 0
    second := 0
    current := 1

    for i := 2; i <= n; i++ {
        first = second
        second = current
        current = first + second + i-3
    }

    return current
}



