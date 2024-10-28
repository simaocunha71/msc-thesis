    words := strings.Split(s, " ")
    result := make([]string, 0)
    for _, word := range words {
        sorted_word := sortString(word)
        result = append(result, sorted_word)
    }
    return strings.Join(result, " ")
}

func sortString(s string) string {
    runes := []rune(s)
    sort.Slice(runes, func(i, j int) bool {
        return runes[i] < runes[j]
    })
    return string(runes)
}