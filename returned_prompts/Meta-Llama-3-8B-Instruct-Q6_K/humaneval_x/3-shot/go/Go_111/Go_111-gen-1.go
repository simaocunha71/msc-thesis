    m := make(map[rune]int)
    if test == "" {
        return m
    }
    words := strings.Split(test, " ")
    for _, word := range words {
        for _, c := range word {
            m[c]++
        }
    }
    max_count := 0
    for count := range m {
        if count == 0 {
            continue
        }
        if count > max_count {
            max_count = count
        }
    }
    result := make(map[rune]int)
    for c, count := range m {
        if count == max_count {
            result[c] = count
        }
    }
    return result
}