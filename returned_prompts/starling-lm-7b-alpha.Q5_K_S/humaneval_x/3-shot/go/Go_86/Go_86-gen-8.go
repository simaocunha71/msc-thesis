    words := strings.Fields(s)
    result := make([]rune, 0)
    for _, w := range words {
        runes := make([]rune, 0)
        for _, r := range w {
            runes = append(runes, r)
        }
        sort.Slice(runes, func(i, j int) bool {
            return runes[i] < runes[j]
        })
        result = append(result, runes...)
        result = append(result, []rune{' '}...)
    }
    return string(result)
}



