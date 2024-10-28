    binary := strconv.FormatInt(int64(N), 2)
    sum := 0
    for _, b := range binary {
        if b == '1' {
            sum++
        }
    }
    return strconv.Itoa(sum)
}

