    for N > 0 {
        N, _ = strconv.Atoi(fmt.Sprintf("%b", N))
    }

    return fmt.Sprintf("%b", N)
}
