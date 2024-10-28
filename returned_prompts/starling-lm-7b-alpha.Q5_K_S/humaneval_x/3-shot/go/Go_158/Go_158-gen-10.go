    type charCounter struct {
        Word string
        Count int
    }
    counts := make(map[string]int)
    for _, word := range words {
        for _, c := range word {
            counts[string(c)]++
        }
    }
    result := ""
    maxCount := 0
    for _, counter := range counts {
        if counter > maxCount {
            maxCount = counter
            result = counts.keys()[counter-1]
        }
    }
    return result
}



