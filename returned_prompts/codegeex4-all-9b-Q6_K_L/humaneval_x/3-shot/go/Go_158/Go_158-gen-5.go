    max_word := ""
    max_count := 0

    for _, word := range words {
        count := 0
        seen := make(map[rune]bool)

        for _, c := range word {
            if !seen[c] {
                count++
                seen[c] = true
            }
        }

        if count > max_count {
            max_count = count
            max_word = word
        }
    }

    return max_word
}



