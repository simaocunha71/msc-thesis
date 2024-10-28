    if len(words) == 0 {
        return ""
    }

    sort.Slice(words, func(i, j int) bool {
        return len(words[i]) < len(words[j])
    })

    unique_chars := make(map[rune]bool)

    for _, word := range words {
        for _, char := range word {
            if _, ok := unique_chars[char]; ok {
                continue
            }
            unique_chars[char] = true
        }
    }

    var max_unique_chars int = 0
    var max_word string = ""

    for _, word := range words {
        var unique_chars_count int = 0
        for _, char := range word {
            if _, ok := unique_chars[char]; ok {
                unique_chars_count += 1
            }
        }
        if unique_chars_count > max_unique_chars {
            max_unique_chars = unique_chars_count
            max_word = word
        }
    }
    return max_word
}



