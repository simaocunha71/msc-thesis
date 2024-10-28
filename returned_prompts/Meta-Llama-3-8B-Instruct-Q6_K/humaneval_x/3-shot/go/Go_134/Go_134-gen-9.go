    words := strings.Split(txt, " ")
    if len(words) == 0 {
        return false
    }
    if len(words[len(words)-1]) == 0 {
        return false
    }
    return strings.ContainsAny(words[len(words)-1], "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") && !strings.Contains(words[len(words)-1], " ")
}