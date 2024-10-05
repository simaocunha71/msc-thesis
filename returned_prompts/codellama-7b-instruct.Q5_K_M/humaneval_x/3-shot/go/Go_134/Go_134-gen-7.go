    if len(txt) == 0 {
        return false
    }
    last_char := string(txt[len(txt) - 1])
    last_char_is_a_letter := (last_char >= "a" && last_char <= "z") || (last_char >= "A" && last_char <= "Z")
    last_char_is_a_word_part := strings.ContainsAny(last_char, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    return last_char_is_a_letter && !last_char_is_a_word_part
}



