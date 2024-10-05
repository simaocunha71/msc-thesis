    bin := strconv.FormatInt(int64(N), 2)
    sum := 0
    for _, v := range bin {
        digit, _ := strconv.Atoi(string(v))
        sum += digit
    }
    return strconv.FormatInt(int64(sum), 2)
}



