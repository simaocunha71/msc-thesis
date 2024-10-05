    result := make(map[rune]bool)
    for _, c := range str {
        if _, ok := result[c]; !ok {
            result[c] = true
        }
    }
    return len(result)
}



