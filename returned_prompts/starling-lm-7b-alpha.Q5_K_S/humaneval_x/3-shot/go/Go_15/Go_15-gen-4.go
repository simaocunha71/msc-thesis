    result := make([]string, n)
    for i := 0; i < n; i++ {
        result[i] = strconv.Itoa(i)
    }
    return string(strings.Join(result, " "))
}



