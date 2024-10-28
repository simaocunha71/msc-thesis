    var maxWord string
    maxUniqueChars := 0

    for _, word := range words {
        uniqueChars := len([]rune(strings.Trim(string(word), string(rune(0x20)))))

        if uniqueChars > maxUniqueChars {
            maxUniqueChars = uniqueChars
            maxWord = word
        } else if uniqueChars == maxUniqueChars {
            if word < maxWord {
                maxWord = word
            }
        }
    }

    return maxWord
}