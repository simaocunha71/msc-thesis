    words := strings.Fields(s)
    for i:=0; i<len(words); i++{
        runes := []rune(words[i])
        sort.Slice(runes, func(i, j int) bool {
            return runes[i] < runes[j]
        })
        words[i] = string(runes)
    }
    return strings.Join(words, " ")
}



