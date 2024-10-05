    words := strings.Split(s, " ")
    var apples, oranges int
    for _, word := range words {
        if strings.HasPrefix(word, "apples") {
            apples, _ = strconv.Atoi(strings.Split(word, " ")[0])
        }
        if strings.HasPrefix(word, "oranges") {
            oranges, _ = strconv.Atoi(strings.Split(word, " ")[0])
        }
    }
    return n - apples - oranges
}