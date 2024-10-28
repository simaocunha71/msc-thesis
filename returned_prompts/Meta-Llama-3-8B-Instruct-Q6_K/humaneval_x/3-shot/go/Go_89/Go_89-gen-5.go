    alphabet := "abcdefghijklmnopqrstuvwxyz"
    result := ""
    for _, char := range s {
        if char >= 'a' && char <= 'z' {
            index := strings.IndexRune(alphabet, char)
            newIndex := (index + 4) % len(alphabet)
            result += string(alphabet[newIndex])
        } else {
            result += string(char)
        }
    }
    return result
}