    counts := make(map[rune]int)
    maxCount := 0
    result := make(map[rune]int)

    for _, letter := range test {
        counts[letter]++
        if counts[letter] > maxCount {
            maxCount = counts[letter]
        }
    }

    for letter, count := range counts {
        if count == maxCount {
            result[letter] = count
        }
    }

    return result
}

