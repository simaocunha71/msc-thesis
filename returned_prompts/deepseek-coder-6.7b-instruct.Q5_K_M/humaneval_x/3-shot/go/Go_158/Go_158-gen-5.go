    sort.Strings(words)
    maxUniqueCount := 0
    maxWord := ""

    for _, word := range words {
        uniqueCount := 0
        used := make([]bool, 26)
        for _, c := range word {
            if !used[c-'a'] {
                used[c-'a'] = true
                uniqueCount++
            }
        }
        if uniqueCount > maxUniqueCount {
            maxUniqueCount = uniqueCount
            maxWord = word
        }
    }

    return maxWord
}



