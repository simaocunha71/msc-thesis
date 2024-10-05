    var max_unique_chars int = 0
    var result string = ""
    for i := 0; i < len(words); i++ {
        var unique_chars int = len(uniqueChars(words[i]))
        if unique_chars > max_unique_chars{
            max_unique_chars = unique_chars
            result = words[i]
        }else if unique_chars == max_unique_chars && words[i] < result {
            result = words[i]
        }
    }
    return result
}

func uniqueChars(word string) string{
    var unique_chars string = ""
    for _, c := range word {
        if !strings.Contains(unique_chars, string(c)) {
            unique_chars += string(c)
        }
    }
    return unique_chars
}



