    words := strings.Split(test, " ")
    histogram := make(map[rune]int)

    for _, word := range words {
        for _, char := range word {
            if count, ok := histogram[char]; ok {
                histogram[char] = count + 1
            } else {
                histogram[char] = 1
            }
        }
    }

    maxCount := 0
    maxChars := make([]rune, 0)

    for char, count := range histogram {
        if count > maxCount {
            maxCount = count
            maxChars = []rune{char}
        } else if count == maxCount {
            maxChars = append(maxChars, char)
        }
    }

    result := make(map[rune]int)
    for _, char := range maxChars {
        result[char] = maxCount
    }

    return result
}