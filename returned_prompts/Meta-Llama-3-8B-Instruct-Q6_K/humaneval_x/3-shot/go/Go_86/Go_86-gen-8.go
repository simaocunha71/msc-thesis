    words := strings.Split(s, " ")
    result := make([]string, 0)

    for _, word := range words {
        chars := []rune(word)
        sort.Slice(chars, func(i, j int) bool {
            return chars[i] < chars[j]
        })
        result = append(result, string(chars))
    }

    return strings.Join(result, " ")
}