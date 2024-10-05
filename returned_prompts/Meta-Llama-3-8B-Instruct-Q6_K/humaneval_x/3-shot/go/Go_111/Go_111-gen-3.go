    words := strings.Split(test, " ")
    result := make(map[rune]int)
    max_count := 0

    for _, word := range words {
        if len(word) > 0 {
            count, ok := result[word[0]]
            if ok {
                result[word[0]] = count + 1
            } else {
                result[word[0]] = 1
            }
            if count + 1 > max_count {
                max_count = count + 1
            }
        }
    }

    max_result := make(map[rune]int)
    for k, v := range result {
        if v == max_count {
            max_result[k] = v
        }
    }

    return max_result
} 





