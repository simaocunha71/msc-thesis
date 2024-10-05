    sort.Strings(words)
    maxUniqueChars := 0
    maxWord := ""

    for _, word := range words {
        uniqueChars := make(map[rune]bool)
        for _, char := range word {
            uniqueChars[char] = true
        }
        if len(uniqueChars) > maxUniqueChars {
            maxUniqueChars = len(uniqueChars)
            maxWord = word
        }
    }

    return maxWord
}



