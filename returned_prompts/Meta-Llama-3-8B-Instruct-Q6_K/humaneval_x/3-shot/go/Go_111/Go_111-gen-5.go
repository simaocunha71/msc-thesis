    words := strings.Split(test, " ")
    result := make(map[rune]int)

    for _, word := range words {
        for _, char := range word {
            count, ok := result[char]
            if ok {
                result[char] = count + 1
            } else {
                result[char] = 1
            }
        }
    }

    max_count := 0
    for _, count := range result {
        if count > max_count {
            max_count = count
        }
    }

    max_result := make(map[rune]int)
    for char, count := range result {
        if count == max_count {
            max_result[char] = count
        }
    }

    return max_result
} 





