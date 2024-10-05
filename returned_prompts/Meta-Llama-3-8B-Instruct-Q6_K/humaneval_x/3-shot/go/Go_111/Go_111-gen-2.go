    if test == "" {
        return map[rune]int{}
    }

    words := strings.Split(test, " ")
    max_count := 0
    result := map[rune]int{}

    for _, word := range words {
        for _, c := range word {
            count, ok := result[c]
            if ok {
                result[c] = count + 1
            } else {
                result[c] = 1
            }
            if count+1 > max_count {
                max_count = count+1
            }
        }
    }

    max_result := map[rune]int{}
    for k, v := range result {
        if v == max_count {
            max_result[k] = v
        }
    }
    return max_result
}