    words := strings.Fields(s)
    result := ""
    for _, word := range words {
        var letters []rune
        for _, letter := range word {
            letters = append(letters, letter)
        }
        sort.Slice(letters, func(i, j int) bool { return letters[i] < letters[j] })
        result += string(letters)
    }
    return result
}



