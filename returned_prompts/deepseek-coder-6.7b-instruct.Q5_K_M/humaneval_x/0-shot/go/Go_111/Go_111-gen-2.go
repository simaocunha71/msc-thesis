    words := strings.Fields(test)
    histogram := make(map[rune]int)

    for _, word := range words {
        for _, letter