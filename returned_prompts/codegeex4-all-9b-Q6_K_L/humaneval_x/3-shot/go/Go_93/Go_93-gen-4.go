    vowels := []string{"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    result := make([]rune, 0)
    for _, c := range message {
        if strings.ContainsRune(strings.Join(vowels, ""), c) {
            result = append(result, rune(int(c)+2))
        } else if c >= 'A' && c <= 'Z' {
            result = append(result, c+32)
        } else if c >= 'a' && c <= 'z' {
            result = append(result, c-32)
        }
    }
    return string(result)
}



