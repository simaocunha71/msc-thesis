    words := strings.Split(s, " ")
    for i, word := range words {
        if strings.HasPrefix(word, "apples") {
            count, _ := strconv.Atoi(strings.Split(word, " ")[0])
            n -= count
        } else if strings.HasPrefix(word, "oranges") {
            count, _ := strconv.Atoi(strings.Split(word, " ")[0])
            n -= count
        }
    }
    return n
}