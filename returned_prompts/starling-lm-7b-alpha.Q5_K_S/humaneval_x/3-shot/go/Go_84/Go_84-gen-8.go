    sum := 0
    for N > 0 {
        sum += N % 2
        N /= 2
    }
    return strconv.FormatInt(int64(sum), 2)
}



