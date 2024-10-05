    binary := strconv.FormatInt(int64(N), 2)
    sum := 0

    for _, c := range binary {
        digit, _ := strconv.Atoi(string(c))
        sum += digit
    }

    return strconv.FormatInt(int64(sum), 2)
}



