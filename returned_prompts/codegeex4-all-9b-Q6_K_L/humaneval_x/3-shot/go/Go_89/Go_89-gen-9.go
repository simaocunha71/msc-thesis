    alphabet := "abcdefghijklmnopqrstuvwxyz"
    encrypted := make([]rune, 0)

    for _, c := range s {
        if !strings.ContainsRune(alphabet, c) {
            encrypted = append(encrypted, c)
        } else {
            index := strings.IndexRune(alphabet, c)
            new_index := (index + 4) % len(alphabet)
            encrypted = append(encrypted, alphabet[new_index])
        }
    }
    return string(encrypted)
}

