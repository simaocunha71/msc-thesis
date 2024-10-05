    binary := strconv.FormatInt(int64(N), 2)
    sum := 0
    for _, v := range binary {
        sum += int(v - '0')
    }
    return strconv.FormatInt(int64(sum), 2)
} 



