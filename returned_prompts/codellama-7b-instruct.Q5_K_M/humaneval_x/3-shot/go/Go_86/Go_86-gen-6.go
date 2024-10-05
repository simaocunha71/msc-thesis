    var result strings.Builder
    for _, word := range strings.Split(s, " ") {
        var sorted_word strings.Builder
        for _, char := range word {
            sorted_word.WriteRune(char)
        }
        sort.Slice(sorted_word.Bytes(), func(i, j int) bool {
            return sorted_word.Bytes()[i] < sorted_word.Bytes()[j]
        })
        result.WriteString(string(sorted_word.Bytes()))
        result.WriteString(" ")
    }
    return strings.TrimSpace(result.String())
}



