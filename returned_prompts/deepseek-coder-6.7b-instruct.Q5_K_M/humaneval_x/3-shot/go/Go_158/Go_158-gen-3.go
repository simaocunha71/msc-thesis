    sort.Strings(words)
    maxCount := 0
    maxWord := ""
    for _, word := range words {
        unique := make(map[rune]struct{})
        for _, char := range word {
            unique[char] = struct{}{}
        }
        count := len(unique)
        if count > maxCount {
            maxCount = count
            maxWord = word
        }
    }
    return maxWord
}



