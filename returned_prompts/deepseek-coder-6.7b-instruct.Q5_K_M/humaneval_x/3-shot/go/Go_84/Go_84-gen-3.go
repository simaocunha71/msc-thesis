    binary := strconv.FormatInt(int64(N), 2)
    sum := 0
    for _, digit := range binary {
        digitInt, _ := strconv.Atoi(string(digit))
        sum += digitInt
    }
    return strconv.FormatInt(int64(sum), 2)
}



