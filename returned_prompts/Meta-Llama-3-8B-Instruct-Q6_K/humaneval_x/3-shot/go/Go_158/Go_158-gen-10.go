    var maxWord string
    maxUniqueChars := 0
    for _, word := range words {
        uniqueChars := len([]rune(word))
        if uniqueChars > maxUniqueChars {
            maxUniqueChars = uniqueChars
            maxWord = word
        }
    }
    return maxWord
} // or
func FindMax(words []string) string {
    var maxWord string
    maxUniqueChars := 0
    for _, word := range words {
        uniqueChars := len([]rune(word))
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
} // or
func FindMax(words []string) string {
    maxWord := words[0]
    maxUniqueChars := 0
    for _, word := range words {
        uniqueChars := len([]rune(word))
        if uniqueChars > maxUniqueChars {
            maxUniqueChars = uniqueChars
            maxWord = word
        }
    }
    return maxWord
} // or
func FindMax(words []string) string {
    maxWord := ""
    maxUniqueChars := 0
    for _, word := range words {
        uniqueChars := len([]rune(word))
        if uniqueChars > maxUniqueChars {
            maxUniqueChars = uniqueChars
            maxWord = word
        }
    }
    return maxWord
} // or
func FindMax(words []string) string {
    sort.Slice(words, func(i, j int) bool {
        word1 := words[i]
        word2 := words[j]
        uniqueChars1 := len([]rune(word1))
        uniqueChars2 := len([]rune(word2))
        if uniqueChars1 > uniqueChars2 {
            return true
        } else if uniqueChars1 == uniqueChars2 {
            return word1 < word2
        }
        return false
    })
    return words[0]
} // or
func FindMax(words []string) string {
    maxWord := words[0]
    maxUniqueChars := 0
    for _, word := range words {
        uniqueChars := len([]rune(word))
        if uniqueChars > maxUniqueChars {
            maxUniqueChars = uniqueChars
            maxWord = word
        }
    }
    return maxWord