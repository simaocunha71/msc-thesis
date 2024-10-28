    sort.Strings(words)
    maxCount := 0
    result := ""

    for _, word := range words {
        uniqueCount := countUniqueCharacters(word)
        if uniqueCount > maxCount {
            maxCount = uniqueCount
            result = word
        }
    }

    return result
}

func countUniqueCharacters(word string) int {
    m := make(map[rune]bool)
    for _, char := range word {
        m[char] = true
    }
    return len(m)
}



