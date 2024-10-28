    var result strings.Builder

    if n == 0 {
        return "0"
    }

    result.WriteString(strconv.Itoa(0))
    result.WriteString(" ")
    result.WriteString(strconv.Itoa(1))
    result.WriteString(" ")

    for i := 2; i <= n; i++ {
        result.WriteString(strconv.Itoa(i))
        result.WriteString(" ")
    }

    return result.String()
}



