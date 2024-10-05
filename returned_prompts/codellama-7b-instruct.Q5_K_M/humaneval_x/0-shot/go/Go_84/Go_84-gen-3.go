    for {
        if N == 0 {
            break A
        }
        N = N / 2
    }
    return strconv.Itoa(N)
}
