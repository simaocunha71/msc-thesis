    result := make(map[rune]bool, 0)
    for _, c := range str {
        result[c] = true
    }
    return len(result)
}



