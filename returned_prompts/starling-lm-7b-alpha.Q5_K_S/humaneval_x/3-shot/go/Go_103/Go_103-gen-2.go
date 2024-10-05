    if n > m {
        return -1
    }
    avg := (n + m) / 2
    binary := fmt.Sprintf("%b", avg)
    return binary
}



