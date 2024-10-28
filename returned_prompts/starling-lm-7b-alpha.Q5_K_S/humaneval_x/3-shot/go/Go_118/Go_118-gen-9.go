    vowels := []rune{'a', 'e', 'i', 'o', 'u'}
    for i := len(word) - 2; i >= 0; i-- {
        if !contains(vowels, word[i]) {
            continue
        }
        for j := i - 1; j >= 0; j-- {
            if !contains(vowels, word[j]) {
                continue
            }
            return string(word[j])
        }
    }
    return ""
}

func contains(slice []rune, item rune) bool {
    for _, v := range slice {
        if v == item {
            return true
        }
    }
    return false
}



