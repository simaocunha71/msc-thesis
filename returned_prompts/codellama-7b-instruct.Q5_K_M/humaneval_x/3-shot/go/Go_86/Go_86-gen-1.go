    var words []string = strings.Split(s, " ")
    var result []string = make([]string, 0, len(words))

    for _, word := range words {
        var letter []rune = make([]rune, 0)
        for _, c := range word {
            letter = append(letter, c)
        }
        sort.Slice(letter, func(i, j int) bool {
            return letter[i] < letter[j]
        })
        result = append(result, string(letter))
    }
    return strings.Join(result, " ")
}



