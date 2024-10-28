    vowels := []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    result := ""
    word_runes := []rune(word)
    for i := 1; i < len(word_runes) - 1; i++ {
        if !contains(vowels, word_runes[i]) {
            continue
        }
        if result == "" {
            result = string(word_runes[i])
            continue
        }
        distance_to_last_vowel := len(word) - (len(word) - i)
        distance_to_next_vowel := i - 1
        if distance_to_next_vowel < distance_to_last_vowel {
            result = string(word_runes[i])
        }
    }
    return result
}

func contains(slice []rune, item rune) bool {
    for _, v := range slice {
        if v == item {
            return true
        }
    }
    return false
}



