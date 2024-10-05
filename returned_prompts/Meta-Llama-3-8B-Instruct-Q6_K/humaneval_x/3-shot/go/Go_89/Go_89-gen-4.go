    alphabet := "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet := alphabet[2:] + alphabet[:2]
    result := make([]byte, 0, len(s))
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            index := int(c - 'a')
            result = append(result, shifted_alphabet[index])
        } else {
            result = append(result, byte(c))
        }
    }
    return string(result)
}