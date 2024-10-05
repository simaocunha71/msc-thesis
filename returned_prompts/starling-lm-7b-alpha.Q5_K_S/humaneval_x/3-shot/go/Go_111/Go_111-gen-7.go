    result := make(map[rune]int)
    char_count := make(map[rune]int)

    for _, c := range test {
        if _, ok := char_count[c]; !ok {
            char_count[c] = 0
        }
        char_count[c] += 1
    }

    for key, count := range char_count {
        result[key] = count
    }

    return result
}



