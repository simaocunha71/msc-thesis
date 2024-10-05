    sort.Strings(words)
    maxCount := 0
    maxWord := ""
    for _, word := range words {
        count := 0
        charMap := make(map[rune]bool)
        for _, char := range word {
            if !charMap[char] {
                charMap[char] = true
                count++
            }
        }
        if count > maxCount {
            maxCount = count
            maxWord = word
        }
    }
    return maxWord
}



