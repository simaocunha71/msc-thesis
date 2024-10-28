    var result strings.Builder
    for i := 0; i <= n; i++ {
        result.WriteString(strconv.Itoa(i))
        result.WriteString(" ")
    }
    return result.String()[:len(result.String())-1]
}




