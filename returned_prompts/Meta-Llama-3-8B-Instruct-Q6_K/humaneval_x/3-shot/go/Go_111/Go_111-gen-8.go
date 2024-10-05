    if len(test) == 0 {
        return map[rune]int{}
    }
    counts := make(map[rune]int)
    words := strings.Split(test, " ")
    for _, word := range words {
        for _, c := range word {
            counts[c]++
        }
    }
    maxCount := 0
    maxLetters := make(map[rune]int)
    for c, count := range counts {
        if count > maxCount {
            maxCount = count
            maxLetters = map[rune]int{c: count}
        } else if count == maxCount {
            maxLetters[c] = count
        }
    }
    return maxLetters
}