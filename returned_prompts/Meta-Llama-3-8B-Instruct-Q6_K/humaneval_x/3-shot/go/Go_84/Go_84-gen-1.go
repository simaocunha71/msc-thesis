    sum := 0
    binary := ""
    for N > 0 {
        remainder := N % 2
        sum += remainder
        binary = strconv.Itoa(remainder) + binary
        N = N / 2
    }
    return binary
}
