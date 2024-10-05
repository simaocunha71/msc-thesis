    if len(words) == 0{
        return ""
    }

    sort.Slice(words, func(i, j int) bool {
        return len(words[i]) > len(words[j])
    })

    unique_chars := make(map[rune]bool)

    max_unique_chars := 0
    result := words[0]

    for _, word := range words {
        unique_chars = make(map[rune]bool)
        for _, ch := range word {
            if _, ok := unique_chars[ch]; !ok {
                unique_chars[ch] = true
                max_unique_chars++
            }
        }

        if max_unique_chars > len(result) {
            result = word
        } else if max_unique_chars == len(result) && word < result {
            result = word
        }
    }

    return result
}



