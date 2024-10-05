    result := make(map[rune]bool)

    for _, c := range str {
        result[c] = true
    }

    return len(result)
}




