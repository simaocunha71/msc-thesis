    binary := strconv.FormatInt(int64(N), 2)
    sum := 0
    for _, c := range binary {
        sum += int(c - '0')
    }
    return strconv.FormatInt(int64(sum), 2)
} 





