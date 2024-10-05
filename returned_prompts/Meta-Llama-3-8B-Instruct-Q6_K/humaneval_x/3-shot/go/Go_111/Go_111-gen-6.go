    counts := make(map[rune]int)
    words := strings.Fields(test)

    for _, word := range words {
        for _, c := range word {
            counts[c]++
        }
    }

    maxCount := 0
    maxCountChars := make([]rune, 0)

    for c, count := range counts {
        if count > maxCount {
            maxCount = count
            maxCountChars = []rune{c}
        } else if count == maxCount {
            maxCountChars = append(maxCountChars, c)
        }
    }

    result := make(map[rune]int)
    for _, c := range maxCountChars {
        result[c] = maxCount
    }
    return result
}