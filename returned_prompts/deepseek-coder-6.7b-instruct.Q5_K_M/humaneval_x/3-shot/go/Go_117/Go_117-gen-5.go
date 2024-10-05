    var words = strings.Fields(s)
    var selectedWords = make([]string, 0)
    var vowels = map[rune]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'A': true, 'E': true, 'I': true, 'O': true, 'U': true}

    for _, word := range words {
        var consonantCount = 0
        for _, letter := range word {
            if _, ok := vowels[letter]; !ok {
                consonantCount++
            }
        }
        if consonantCount == n {
            selectedWords = append(selectedWords, word)
        }
    }

    return selectedWords
}



