    var result string
    words := strings.Split(sentence, " ")
    for _, word := range words {
        if len(word) > 1 && IsPrime(len(word)) {
            result += word + " "
        }
    }
    return strings.TrimSpace(result)
}



