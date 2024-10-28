    sort.Strings(words)
    maxCount, maxWord := 0, ""
    for _, word := range words {
        unique := make(map[rune]struct{})
        for _, ch := range word {
            unique[ch] = struct{}{}
        }
        count := len(unique)
        if count > maxCount {
            maxCount, maxWord = count, word
        }
    }
    return maxWord
}



