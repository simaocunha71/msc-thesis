    vowels := []rune{'a', 'e', 'i', 'o', 'u', 'y'}
    var result []rune

    for _, c := range text {
        if !contains(vowels, c) {
            result = append(result, c)
        }
    }
    return string(result)
}

func contains(slice []rune, element rune) bool {
    for _, item := range slice {
        if item == element {
            return true
        }
    }
    return false
}



