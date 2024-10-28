    binary := strconv.FormatInt(int64(N), 2)
    sum := 0
    for _, c := range binary {
        if c == '1' {
            sum += 1
        }
    }
    return strconv.Itoa(sum)
}