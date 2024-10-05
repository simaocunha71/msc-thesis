    vowels := "aeiouAEIOU"
    new_string := make([]rune, 0)

    for _, c := range message {
        if strings.ContainsRune(vowels, c) {
            new_string = append(new_string, rune(c+2))
        } else if strings.ContainsRune(strings.ToUpper(vowels), c) {
            new_string = append(new_string, rune(c-2))
        } else {
            new_string = append(new_string, c)
        }
    }
    return string(new_string)
}

