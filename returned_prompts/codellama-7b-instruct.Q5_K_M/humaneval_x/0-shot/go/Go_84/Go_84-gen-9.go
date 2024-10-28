    for {
        if N < 1 {
            break A
        }
        if N%2 == 0 {
            N = N/2
        } else {
            N = (N-1)/2 + 1
        }
    }
    return strconv.Itoa(N)
}
