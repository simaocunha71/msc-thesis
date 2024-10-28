    vowels := []rune{'A', 'E', 'I', 'O', 'U'}
    result := 0
    for i, r := range s {
        if i % 2 == 0 && contains(vowels, r) {
            result += 1
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



