    binary := strconv.FormatInt(int64(N), 2)
    var sum int
    for _, c := range binary {
        if c == '1' {
            sum += 1
        }
    }
    return strconv.Itoa(sum)
}