    words := strings.Fields(s)
    for i := range words {
        chars := strings.Split(words[i], "")
        sort.Strings(chars)
        words[i] = strings.Join(chars, "")
    }
    return strings.Join(words, " ")
}



