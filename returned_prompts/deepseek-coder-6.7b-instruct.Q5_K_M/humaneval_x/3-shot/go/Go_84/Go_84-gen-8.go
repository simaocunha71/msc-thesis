    sum := 0
    for N > 0 {
        digit := N % 10
        sum += digit
        N /= 10
    }

    return strconv.FormatInt(int64(sum), 2)
}



