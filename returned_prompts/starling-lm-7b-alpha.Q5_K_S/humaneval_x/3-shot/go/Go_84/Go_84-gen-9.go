    result := 0
    for i := 0; i < len(strconv.Itoa(N)); i++ {
        result += int(strconv.Itoa(N)[i] - '0')
    }
    return strconv.FormatInt(int64(result), 2)
}



