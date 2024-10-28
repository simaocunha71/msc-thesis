    result := make([]rune, 0)
    for x > 0 {
        result = append(result, rune(strconv.FormatInt(int64(x) % base, 10)[0]))
        x /= base
    }
    return string(result)
}



