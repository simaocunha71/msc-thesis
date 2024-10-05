    binary := strconv.FormatInt(int64(N), 2)
    sum := 0
    for _, v := range binary {
        num, _ := strconv.Atoi(string(v))
        sum += num
    }
    return strconv.Itoa(sum)
}

