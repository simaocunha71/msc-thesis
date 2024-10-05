    for ; N >= 2; N /= 2 {
        if N%2 == 1 {
            goto A
        }
    }
    return strconv.Itoa(N)
}

