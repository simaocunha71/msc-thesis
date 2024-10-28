    words := strings.Split(test, " ")
    result := make(map[rune]int)
    for _, word := range words {
        for _, c := range word {
            count, ok := result[c]
            if ok {
                result[c] = count + 1
            } else {
                result[c] = 1
            }
        }
    }
    maxCount := 0
    for _, count := range result {
        if count > maxCount {
            maxCount = count
        }
    }
    for c, count := range result {
        if count == maxCount {
            result[c] = count
        } else {
            delete(result, c)
        }
    }
    return result
}