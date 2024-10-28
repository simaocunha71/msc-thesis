    words := strings.Split(test, " ")
    result := make(map[rune]int)

    for _, word := range words {
        for _, c := range word {
            count, ok := result[c]
            if !ok {
                result[c] = 1
            } else {
                result[c] = count + 1
            }
        }
    }
    maxCount := 0
    var maxChars []rune
    for c, count := range result {
        if count > maxCount {
            maxCount = count
            maxChars = []rune{c}
        } else if count == maxCount {
            maxChars = append(maxChars, c)
        }
    }
    return map[rune]int{c: count for _, c := range maxChars}
}