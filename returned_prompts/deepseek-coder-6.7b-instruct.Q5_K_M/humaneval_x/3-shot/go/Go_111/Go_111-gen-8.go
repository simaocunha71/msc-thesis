    letterCounts := make(map[rune]int)
    maxCount := 0
    result := make(map[rune]int)

    for _, letter := range test {
        letterCounts[letter]++
        if letterCounts[letter] > maxCount {
            maxCount = letterCounts[letter]
        }
    }

    for letter, count := range letterCounts {
        if count == maxCount {
            result[letter] = count
        }
    }

    return result
}



