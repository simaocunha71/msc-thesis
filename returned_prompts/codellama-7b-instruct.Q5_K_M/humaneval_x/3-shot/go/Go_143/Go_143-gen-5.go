    var result strings.Builder
    words := strings.Split(sentence, " ")
    for _, word := range words {
        if IsPrime(len(word)) {
            result.WriteString(word)
            result.WriteString(" ")
        }
    }
    return strings.TrimSpace(result.String())
}



