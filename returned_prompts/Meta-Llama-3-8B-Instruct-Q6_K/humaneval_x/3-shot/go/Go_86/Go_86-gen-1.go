    words := strings.Split(s, " ")
    result := make([]string, 0)

    for _, word := range words {
        sorted_word := sort.StringSlice(strings.Split(word, ""))
        sorted_word.Sort()
        result = append(result, strings.Join(sorted_word, ""))
    }
    return strings.Join(result, " ")
}
}:



