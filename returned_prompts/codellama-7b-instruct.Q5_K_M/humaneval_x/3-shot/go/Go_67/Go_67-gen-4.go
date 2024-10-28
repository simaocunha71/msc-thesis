    s = strings.Trim(s, " ")
    s = strings.ReplaceAll(s, "apples", "")
    s = strings.ReplaceAll(s, "oranges", "")
    s = strings.ReplaceAll(s, "and", "")
    s = strings.ReplaceAll(s, " ", "")
    result, _ := strconv.Atoi(s)
    return n - result
}




