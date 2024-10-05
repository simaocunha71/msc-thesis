    result := make([]rune, 0)
    alphabet := "abcdefghijklmnopqrstuvwxyz"
    for _, c := range strings.ToLower(s) {
        if c >= 'a' && c <= 'z' {
            index := int(c - 'a')
            encrypted_index := (index + 4*2) % 26
            encrypted_char := rune(alphabet[encrypted_index] + 'a' - 1)
            result = append(result, encrypted_char)
        } else {
            result = append(result, c)
        }
    }
    return string(result)
}