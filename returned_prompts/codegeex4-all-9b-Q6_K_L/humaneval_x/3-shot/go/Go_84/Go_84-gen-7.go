    binary := strconv.FormatInt(int64(N), 2)
    sum := 0
    for _, c := range binary {
        i, _ := strconv.Atoi(string(c))
        sum += i
    }
    return strconv.Itoa(sum)
}



