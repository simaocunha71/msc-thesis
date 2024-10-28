    words := strings.Split(s, " ")
    var result []string
    for _, word := range words {
        consonants := 0
        for _, c := range word {
            if !strings.ContainsRune("aeiou", c) && c != ' ' {
                consonants++
            }
        }
        if consonants == n {
            result = append(result, word)
        }
    }
    return result
}



