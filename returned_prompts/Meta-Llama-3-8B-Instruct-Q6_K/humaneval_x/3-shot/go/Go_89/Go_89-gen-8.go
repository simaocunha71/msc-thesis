    alphabet := "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet := ""
    for _, char := range alphabet {
        if strings.Contains(alphabet, string(char)) {
            index := strings.Index(alphabet, string(char))
            new_index := (index + 4) % 26
            shifted_alphabet += string(alphabet[new_index])
        }
    }
    result := ""
    for _, char := range s {
        if strings.Contains(alphabet, string(char)) {
            index := strings.Index(alphabet, string(char))
            new_index := (index + 4) % 26
            result += string(shifted_alphabet[new_index])
        } else {
            result += string(char)
        }
    }
    return result
}  // Output: lmgw, ewhjklmn, kjo, ixj


