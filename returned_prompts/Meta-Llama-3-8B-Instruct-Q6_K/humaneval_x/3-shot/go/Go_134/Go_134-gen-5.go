    words := strings.Split(txt, " ")
    if len(words) > 0 {
        last_word := words[len(words)-1]
        if len(last_word) > 0 {
            return !strings.ContainsAny(last_word, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        }
    }
    return false
}