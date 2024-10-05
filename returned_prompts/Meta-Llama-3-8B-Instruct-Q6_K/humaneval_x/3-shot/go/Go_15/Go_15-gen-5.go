    result := ""
    for i := 0; i <= n; i++ {
        result += strconv.Itoa(i)
        if i < n {
            result += " "
        }
    }
    return result
}