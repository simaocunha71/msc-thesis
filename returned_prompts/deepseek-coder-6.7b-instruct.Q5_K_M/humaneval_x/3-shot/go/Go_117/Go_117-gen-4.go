    var words []string = strings.Split(s, " ")
    var consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    var result []string

    for _, word := range words {
        count := 0
        for _, letter := range word {
            if strings.ContainsRune(consonants, letter) {
                count++
            }
        }
        if count == n {
            result = append(result, word)
        }
    }

    return result
}



