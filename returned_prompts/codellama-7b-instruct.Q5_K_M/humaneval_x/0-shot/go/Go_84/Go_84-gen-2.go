    for i := 0; i < 10; i++ {
        if N%2 == 0 {
            N = N / 2
            continue A
        } else {
            N = N / 2 + 1
            continue A
        }
    }
    return strconv.Itoa(N)
}