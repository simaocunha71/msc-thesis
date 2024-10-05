    words := strings.Split(s, " ")
    count := 0
    for _, word := range words {
        if strings.HasPrefix(word, "apples") {
            count, _ = strconv.Atoi(strings.Split(word, " ")[0])
        }
        if strings.HasPrefix(word, "oranges") {
            count, _ = strconv.Atoi(strings.Split(word, " ")[0])
        }
    }
    return n - count
} 