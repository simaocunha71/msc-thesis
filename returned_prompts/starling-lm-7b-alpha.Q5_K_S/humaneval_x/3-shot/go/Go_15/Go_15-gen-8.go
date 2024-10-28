    result := make([]string, 0)
    for i := 0; i <= n; i++ {
        result = append(result, strconv.Itoa(i))
    }
    return strings.Join(result, " ")
}



