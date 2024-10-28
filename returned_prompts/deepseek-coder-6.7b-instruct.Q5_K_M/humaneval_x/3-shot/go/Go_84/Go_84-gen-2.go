    sum := 0
    binaryString := ""
    binary := strconv.FormatInt(int64(N), 2)
    for _, b := range binary {
        digit, _ := strconv.Atoi(string(b))
        sum += digit
    }
    binaryString = strconv.FormatInt(int64(sum), 2)
    return binaryString
}



