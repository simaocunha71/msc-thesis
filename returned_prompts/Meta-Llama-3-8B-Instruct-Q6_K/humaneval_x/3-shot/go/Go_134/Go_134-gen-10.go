    words := strings.Split(txt, " ")
    if len(words) > 0 {
        last_word := words[len(words) - 1]
        return len(last_word) > 0 && !strings.Contains(last_word, " ")
    }
    return false
}