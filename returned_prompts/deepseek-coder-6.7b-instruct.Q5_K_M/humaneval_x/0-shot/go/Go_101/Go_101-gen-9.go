    var words []string
    word := ""
    for _, c := range s {
        if c == ' ' || c == ',' {
            if word != "" {
                words = append(words, word)
                word = ""
            }
        } else {
            word += string(c)
        }
    }
    if word != "" {
        words = append(words, word)
    }
    return words
}


