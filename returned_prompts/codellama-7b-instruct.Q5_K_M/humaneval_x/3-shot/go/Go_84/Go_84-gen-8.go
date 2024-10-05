    var sum int
    for N > 0 {
        remainder := N % 2
        sum += remainder
        N = N / 2
    }
    return strconv.Itoa(sum)
}



