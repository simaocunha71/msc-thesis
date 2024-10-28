    var words = strings.Split(s, " ")
    var result = make([]byte, 0)

    for _, word := range words {
        sorted_word := make([]byte, 0)
        for _, c := range word {
            sorted_word = append(sorted_word, c)
        }
        sort.Slice(sorted_word, func(i, j int) bool { return sorted_word[i] < sorted_word[j] })

        result = append(result, sorted_word...)
        result = append(result, []byte{ ' ' })
    }
    return string(result)
}



