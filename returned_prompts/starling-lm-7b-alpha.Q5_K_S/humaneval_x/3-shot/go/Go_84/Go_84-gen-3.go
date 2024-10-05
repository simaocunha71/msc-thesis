    sum := 0
    for n := N; n > 0; n /= 2 {
        sum += n % 2
    }
    return strconv.FormatInt(int64(sum), 2)
}



