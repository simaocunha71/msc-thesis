    distinct_characters := make(map[rune]bool)

    for _, c := range strings.ToLower(str) {
        distinct_characters[c] = true
    }

    return len(distinct_characters)
}



