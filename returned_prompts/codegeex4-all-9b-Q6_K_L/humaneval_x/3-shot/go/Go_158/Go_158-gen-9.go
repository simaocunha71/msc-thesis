    max := 0
    result := ""
    for _, word := range words {
        unique := make(map[rune]struct{})
        for _, c := range word {
            unique[c] = struct{}{}
        }
        if len(unique) > max {
            max = len(unique)
            result = word
        }
    }
    return result
}



